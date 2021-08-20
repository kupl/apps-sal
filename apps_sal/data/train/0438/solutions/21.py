class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        sizes = collections.defaultdict(int)
        has = [0] * len(arr)
        ends = {}
        out = 0
        for (i, a) in enumerate(arr):
            has[a - 1] += 1
            if a - 1 in ends and a + 1 in ends:
                length1 = a - 1 - ends[a - 1] + 1
                length2 = ends[a + 1] + 1 - (a + 1)
                temp1 = ends[a + 1]
                temp2 = ends[a - 1]
                ends[temp2] = temp1
                ends[temp1] = temp2
                sizes[length1] -= 1
                sizes[length2] -= 1
                sizes[length1 + 1 + length2] += 1
            elif a - 1 in ends:
                length1 = a - 1 - ends[a - 1] + 1
                ends[a] = ends[a - 1]
                ends[ends[a - 1]] = a
                sizes[length1] -= 1
                sizes[length1 + 1] += 1
            elif a + 1 in ends:
                length1 = ends[a + 1] - (a + 1) + 1
                ends[a] = ends[a + 1]
                ends[ends[a + 1]] = a
                sizes[length1] -= 1
                sizes[length1 + 1] += 1
            else:
                ends[a] = a
                sizes[1] += 1
            if sizes[m] > 0:
                out = i + 1
        return out if out else -1
