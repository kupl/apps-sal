class Group:
    def __init__(self, x, y):
        self.left = x
        self.right = y
        self.n = y - x + 1


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        groups = [None] * (1 + len(arr))
        group_size = collections.defaultdict(int)
        visited = set()
        res = -1
        for step, x in enumerate(arr, 1):
            visited.add(x)
            left = right = x
            lsize = rsize = 0
            if x > 1 and x - 1 in visited:
                left = groups[x - 1].left
                lsize = groups[x - 1].n
            if x < len(arr) and x + 1 in visited:
                right = groups[x + 1].right
                rsize = groups[x + 1].n
            g = Group(left, right)
            groups[left] = g
            groups[right] = g
            group_size[lsize + rsize + 1] += 1
            if lsize != 0:
                group_size[lsize] -= 1
            if rsize != 0:
                group_size[rsize] -= 1

            if group_size[m] > 0:
                res = step
        return res
