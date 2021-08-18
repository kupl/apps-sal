class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        n = len(arr)
        p = [i for i in range(n + 1)]
        count = [0] * (n + 1)
        groups = [0] * (n + 1)

        def findp(x):
            while x != p[x]:
                x = p[x]
            return x

        def union(x, y):

            groups[count[y]] -= 1
            groups[count[x]] -= 1
            if count[x] >= count[y]:
                p[y] = x
                count[x] += count[y]
                groups[count[x]] += 1
            else:
                p[x] = y
                count[y] += count[x]
                groups[count[y]] += 1

        res = -1

        for i, num in enumerate(arr):
            count[num] = 1
            left = num - 1
            right = num + 1
            groups[1] += 1
            if left >= 1 and count[left] != 0:
                pl = findp(left)
                pm = findp(num)
                if pl != pm:
                    union(pl, pm)
            if right <= n and count[right] != 0:
                pr = findp(right)
                pm = findp(num)
                if pr != pm:
                    union(pr, pm)

            if groups[m] > 0:
                res = i + 1
        return res
