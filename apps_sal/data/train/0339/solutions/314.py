class Solution:

    def numTriplets(self, a: List[int], b: List[int]) -> int:
        map1 = {}
        map2 = {}
        for i in range(len(a)):
            for j in range(len(a)):
                if i != j:
                    if a[i] * a[j] not in map1.keys():
                        map1[a[i] * a[j]] = 0
                    map1[a[i] * a[j]] += 1
        for i in range(len(b)):
            for j in range(len(b)):
                if i != j:
                    if b[i] * b[j] not in map2.keys():
                        map2[b[i] * b[j]] = 0
                    map2[b[i] * b[j]] += 1
        count = 0
        for i in a:
            if i * i in map2.keys():
                count += map2[i * i]
        for i in b:
            if i * i in map1.keys():
                count += map1[i * i]
        return count // 2
