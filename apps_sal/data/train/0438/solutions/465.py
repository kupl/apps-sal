from collections import defaultdict


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)

        if m == n:
            return m

        # number at index i means the length of 1's array starting or ending at i
        b = [0] * (n + 2)
        cnt = defaultdict(lambda: 0)
        latest = -1
        for i in range(n):
            left = b[arr[i] - 1]
            right = b[arr[i] + 1]

            # if left is non-zero, arr[i]-1 must be the end of a 1's array
            # it cannot be a start because arr[i] is not yet 1
            # in this case we merge with left, arr[i] will be the new end point
            if left > 0 and right == 0:
                # b[arr[i]-1]+=1
                b[arr[i]] += 1 + left
                # arr[i]-1-left-1 is the start of the 1's array
                b[arr[i] - 1 - left + 1] += 1
                cnt[left] -= 1
                cnt[left + 1] += 1
            elif left == 0 and right > 0:
                # b[arr[i]+1]+=1
                b[arr[i]] += 1 + right
                # arr[i]+1+right-1 is the end of the 1's array
                b[arr[i] + 1 + right - 1] += 1
                cnt[right] -= 1
                cnt[right + 1] += 1
            # if both are non zero, we can merge the left array and right array
            # creating an array with length left + right + 1
            elif left > 0 and right > 0:
                # b[arr[i]-1]+=1+right
                # b[arr[i]+1]+=1+left
                # b[arr[i]]+=1+left+right

                # arr[i]-1-left-1 is the start of the 1's array
                b[arr[i] - 1 - left + 1] += 1 + right
                # arr[i]+1+right-1 is the end of the 1's array
                b[arr[i] + 1 + right - 1] += 1 + left
                cnt[right] -= 1
                cnt[left] -= 1
                cnt[1 + left + right] += 1
            else:  # final case where both left and right are zero
                b[arr[i]] += 1
                cnt[1] += 1
            if m in cnt:
                if cnt[m] > 0:
                    latest = i + 1
        return latest
