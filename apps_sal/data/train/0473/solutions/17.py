class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xors = [arr[0]]

        for i in range(1, len(arr)):
            xors.append(xors[-1] ^ arr[i])

        print(xors)
        n = len(arr)
        count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                temp = xors[j]
                if i > 0:
                    temp ^= xors[i - 1]

                if temp == 0:
                    count += j - i

        return count
