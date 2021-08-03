class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)

        # create union
        maxA = max(A)
        unionL = list(range(maxA + 1))  # initialize, each one is a component itself
        size = [1] * (maxA + 1)  # every component has size 1, the element itself initially

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
                    unionL[k1] = k2  # can improve with size
                    size[k2] += size[k1]
                else:
                    unionL[k2] = k1  # can improve with size
                    size[k1] += size[k2]
            return

        for item in A:
            mid = int(math.sqrt(item)) + 1
            for k in range(2, mid + 1):  # mid included
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
