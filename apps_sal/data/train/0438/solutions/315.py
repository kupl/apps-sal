class Subsets:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent


def union(subsets, x, y):

    xr = find(subsets, x)
    yr = find(subsets, y)

    if xr == yr:
        return False
    else:

        xr = subsets[xr]
        yr = subsets[yr]

        r1 = xr.rank
        r2 = yr.rank

        if r1 < r2:
            xr.parent = yr.parent
            yr.rank += xr.rank
        elif r2 < r1:
            yr.parent = xr.parent
            xr.rank += yr.rank
        else:
            xr.parent = yr.parent
            yr.rank += xr.rank

        return True


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:

        subsets = [Subsets(i, 1) for i in range(len(arr))]
        lst = [0] * len(arr)
        parents = set()
        ans = -1
        time = 1

        for index in arr:

            index -= 1
            lst[index] = 1

            if index + 1 < len(arr) and lst[index + 1] == 1:
                p = find(subsets, index + 1)
                if p in parents:
                    parents.remove(p)
                union(subsets, index + 1, index)

            if index - 1 >= 0 and lst[index - 1] == 1:
                p = find(subsets, index - 1)
                if p in parents:
                    parents.remove(p)
                union(subsets, index - 1, index)

            if subsets[find(subsets, index)].rank == m:
                parents.add(find(subsets, index))

            if len(parents):
                ans = time

            time += 1

        return ans
