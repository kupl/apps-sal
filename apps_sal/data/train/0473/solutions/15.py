class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        prefix = [arr[0]]
        for i in range(1, len(arr)):
            prefix.append(prefix[-1] ^ arr[i])

        ans = 0
        for i in range(1, len(prefix)):
            for j in range(i + 1, len(prefix)):
                if prefix[i - 1] ^ prefix[j] == 0:
                    ans += j - i
        for i in range(len(prefix)):
            if prefix[i] == 0:
                ans += i
        return ans
