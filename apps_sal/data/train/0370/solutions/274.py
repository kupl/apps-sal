from collections import defaultdict as dd


def find(parent, num):
    if parent[num] == -1:
        return num
    else:
        parent[num] = find(parent, parent[num])
    return parent[num]


def union(parent, u, v):
    par_u = find(parent, u)
    par_v = find(parent, v)
    if par_u != par_v:
        parent[par_v] = par_u


class Solution:

    def largestComponentSize(self, a: List[int]) -> int:
        ans = 0
        n = len(a)
        parent = [-1] * 100001
        for i in range(n):
            x = a[i]
            for j in range(2, int(x ** 0.5) + 1):
                if x % j == 0:
                    union(parent, j, x)
                    union(parent, x // j, x)
        count = dd(int)
        for i in range(len(a)):
            par = find(parent, a[i])
            count[par] += 1
            ans = max(ans, count[par])
        return ans
