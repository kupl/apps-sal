class Solution:
    def validateBinaryTreeNodes(self, n: int, left: List[int], right: List[int]) -> bool:

        children = {}
        nodes = {}

        for i in range(n):
            l, r = left[i], right[i]

            if (l != -1 and l in children) or (r != -1 and r in children):
                print('Here Yo-', children, l, r)
                return False
            elif i in children and children[i] in [l, r]:
                print('Baap ko gali')
                return False
            elif i in [l, r]:
                print('Selfie')
                return False

            nodes[i] = [l, r]
            children[l] = i
            children[r] = i

        root = 0
        for i in range(n):
            if i not in children:
                root = i
                break

        count = 0
        frontier = [root]
        seen = set()
        while frontier:
            cur = frontier.pop()
            if cur == -1:
                continue
            count += 1
            c = nodes[cur]
            if (c[0] != -1 and c[0] in seen) or (c[1] != -1 and c[1] in seen):
                return False

            if c[0] != -1:
                seen.add(c[0])
                frontier.append(c[0])
            if c[1] != -1:
                seen.add(c[1])
                frontier.append(c[1])

        if count != n:
            return False
        return True
