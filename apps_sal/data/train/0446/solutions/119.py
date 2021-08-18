class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        from collections import Counter

        counter = Counter(arr)

        counter = sorted(counter.most_common(), key=lambda x: (x[1], x[0]), reverse=True)

        while k > 0 and counter:

            edge = list(counter[-1])

            edge[1] -= 1

            counter[-1] = tuple(edge)

            if counter[-1][1] == 0:
                counter.pop()

            k -= 1

        return len(counter)
