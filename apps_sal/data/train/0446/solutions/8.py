from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        L = len(arr)
        d = [[] for _ in range(L+1)]
        counter = Counter(arr)

        for key, count in list(counter.items()):
            d[count].append(key)
        
        for count in range(L+1):
            if k == 0:
                break

            while d[count] and k >= count:
                item = d[count].pop()
                del counter[item]
                k -= count

        return len(counter)

