class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefixxor = [0]

        for i in range(n):
            prefixxor.append(prefixxor[- 1] ^ arr[i])

        count = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j, n + 1):
                    if prefixxor[j - 1] ^ prefixxor[i - 1] == prefixxor[k] ^ prefixxor[j - 1]:
                        count += 1
        return count
