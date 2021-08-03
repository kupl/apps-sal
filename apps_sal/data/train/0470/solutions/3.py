from collections import Counter


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:

        MAX = 10**9 + 7
        count = collections.Counter(A)
        keys = sorted(count)
        ans = 0
        for i, x in enumerate(keys):

            j = i
            k = len(keys) - 1

            while(j <= k):
                y, z = keys[j], keys[k]
                sum_t = x + y + z

                if sum_t < target:
                    j += 1
                elif(sum_t > target):
                    k -= 1

                else:

                    if(i < j < k):
                        ans += count[x] * count[y] * count[z]

                    elif (x == y and y < z):
                        ans += (count[x] * (count[x] - 1) * count[z]) // 2

                    elif(x < y and y == z):
                        ans += (count[x] * (count[y]) * (count[y] - 1)) // 2

                    else:
                        ans += (count[x] * (count[x] - 1) * (count[x] - 2)) // 6

                    j += 1
                    k -= 1

        return ans % MAX
