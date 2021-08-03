class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        preXor = [0] * (len(arr) + 1)

        for i, element in enumerate(arr):
            preXor[i + 1] = preXor[i] ^ element

        count = 0
        for i in range(len(arr)):

            for j in range(i + 1, len(arr)):

                for k in range(j, len(arr)):

                    a = preXor[j] ^ preXor[i]

                    b = preXor[k + 1] ^ preXor[j]

                    if a == b:
                        count += 1

        return count
