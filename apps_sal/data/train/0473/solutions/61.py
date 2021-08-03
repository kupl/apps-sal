class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xor = [arr[0]]
        answer = 0

        for i in range(1, len(arr)):
            prefix_xor.append(prefix_xor[i - 1] ^ arr[i])

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):

                a = prefix_xor[j]

                if i > 0:
                    a = a ^ prefix_xor[i - 1]

                for k in range(j, len(arr)):
                    b = prefix_xor[k] ^ prefix_xor[j]

                    if a == b:
                        answer += 1

        return answer
