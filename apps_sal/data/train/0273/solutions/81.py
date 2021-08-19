class Solution:
    def racecar(self, target: int) -> int:
        dp = [0, 1, 4] + [float('inf')] * target
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]

#         f = [None] * (target + 1)

#         f[0] = 0

#         for i in range(1, target + 1):
#             f[i] = float('inf')

#             n = len(bin(i)[2:])

#             if 2**n - 1 == i:
#                 f[i] = n
#                 continue

#             # overspeed
#             f[i] = f[2**n - 1 - i] + n + 1 # reverse once

#             # underspeed
#             for j in range(0, n):
#                 gap = 1 << j - 1
#                 f[i] = min(f[i], f[i - 2**(n - 1) + gap] + n + j + 1) # reverse twice
#         return f[target]


#         int[] f = new int[target + 1];
#         for (int i = 1; i <= target; i++){
#             int bound = (Integer.highestOneBit(i) << 1) - 1;
#             int n = Integer.bitCount(bound);
#             if (i == bound){
#                 f[i] = n;
#                 continue;
#             }
#             // overspeed
#             f[i] = f[bound - i] + n + 1; // Reverse once
#             // underspeed
#             bound >>= 1;
#             for (int j = 0; j < n; j++){
#                 int gap = (1 << j) - 1;
#                 f[i] = Math.min(f[i], f[i - bound + gap] + n + j + 1); // Reverse twice
#             }
#         }
#         return f[target];
#     }
# }
