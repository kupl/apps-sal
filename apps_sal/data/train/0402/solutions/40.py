class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        CANNOT_MEET = 0
        CAN_WALK_200_STEPS = 1
        CAN_MEET = 2
        blocked_set = set(tuple(element) for element in blocked)
        
        def is_valid(i, j, seen):
            return 0 <= i < 10 ** 6 and 0 <= j < 10 ** 6 and (i, j) not in blocked_set and (i, j) not in seen
        
        def can_meet(source, target):
            i, j = source
            ti, tj = target
            q = deque([(i, j, 0)])
            seen = set()
            seen.add((i, j))
            while q:
                i, j, step = q.popleft()
                if (i == ti and j == tj):
                    return CAN_MEET
                if step == 200:
                    return CAN_WALK_200_STEPS
                for di, dj in DELTAS:
                    i1, j1 = i + di, j + dj
                    if is_valid(i1, j1, seen):
                        seen.add((i1, j1))
                        q.append((i1, j1, step + 1))
            return CANNOT_MEET
        
        result1 = can_meet(source, target)
        if result1 == CANNOT_MEET:
            return False
        if result1 == CAN_MEET:
            return True
        
        # result1 == CAN_WALK_200_STEPS
        result2 = can_meet(target, source)
        if result2 == CAN_WALK_200_STEPS:
            return True
        return False

