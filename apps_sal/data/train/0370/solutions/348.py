class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)

        maxA = max(A)
        unionL = list(range(maxA + 1))
        size = [1] * (maxA + 1)

        def findRoot(i):
            k1 = i
            while unionL[k1] != k1:
                unionL[k1] = unionL[unionL[k1]]
                k1 = unionL[k1]
            return k1

        def union(x, y):
            k1 = findRoot(x)
            k2 = findRoot(y)
            if k1 != k2:
                if size[k1] < size[k2]:
                    unionL[k1] = k2
                    size[k2] += size[k1]
                else:
                    unionL[k2] = k1
                    size[k1] += size[k2]
            return

        for item in A:
            mid = int(math.sqrt(item)) + 1
            for k in range(2, mid + 1):
                if item % k == 0:
                    union(item, k)
                    if item // k != 1:
                        union(item, item // k)

        count = {}
        for item in A:
            root = findRoot(item)
            if root in count:
                count[root] += 1
            else:
                count[root] = 1

        return max(count.values())
