class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        block_set = {tuple(t) for t in blocked}
        source, target = tuple(source), tuple(target)
        if source in block_set or target in block_set:
            return False

        def findPath(source, target, block_set):
            from collections import deque
            queue = deque()
            covered, covered_block = set(), set()
            queue.append(source)
            covered.add(source)
            while len(queue) > 0:
                count = len(queue)
                while count > 0:
                    head = queue.popleft()
                    count -= 1
                    for dir1 in directions:
                        x, y = head[0] + dir1[0], head[1] + dir1[1]
                        if x < 0 or x == int(1e6) or y < 0 or y == int(1e6):
                            continue
                        pos = (x, y)
                        if pos == target:
                            return True
                        elif pos in covered:
                            continue
                        elif pos in block_set:
                            covered.add(pos)
                            covered_block.add(pos)
                        else:
                            queue.append(pos)
                            covered.add(pos)

                if len(queue) + len(covered_block) > len(block_set):
                    return True
            return False

        if not findPath(source, target, block_set):
            return False

        return findPath(target, source, block_set)
