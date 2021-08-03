class Solution:
    def threeSum(self, A: List[int], target: int) -> List[List[int]]:
        triples = []

        i = 0
        k = len(A) - 1
        while i <= k:
            j = i
            k = len(A) - 1
            while j <= k:
                if A[j] + A[k] < target - A[i]:
                    j += 1
                elif A[j] + A[k] > target - A[i]:
                    k -= 1
                else:
                    triples.append([A[i], A[j], A[k]])
                    j += 1
                    k -= 1
            i += 1
        return triples

    def threeSumMulti(self, A: List[int], target: int) -> int:
        res = 0
        count = {}
        for num in A:
            count[num] = count.get(num, 0) + 1
        sorted_A_no_dup = sorted([num for num in count])

        all_triples = self.threeSum(sorted_A_no_dup, target)
        for triple in all_triples:
            a, b, c = triple[0], triple[1], triple[2]
            if a != b and b != c:
                res += count[a] * count[b] * count[c]
            elif a == b and b != c:
                res += count[a] * (count[a] - 1) * count[c] // 2
            elif a != b and b == c:
                res += count[a] * count[b] * (count[b] - 1) // 2
            elif a == b and b == c:
                res += count[a] * (count[a] - 1) * (count[a] - 2) // 6
            res %= 10**9 + 7
        return res
