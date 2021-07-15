class Solution:
    def superEggDrop(self, eggs: int, floors: int) -> int:
        
        dp = [[-1 for _ in range(floors+1)] for _ in range(eggs+1)]
        
#         int dp(int k, int n) {
#             if (k <= 0) return 0;
#             if (k == 1) return n;
#             if (n <= 1) return n;
#             if (m_[k][n] != INT_MIN) return m_[k][n];

#             // broken[i]   = dp(k - 1, i - 1) is incresing with i.
#             // unbroken[i] = dp(k,     n - i) is decresing with i.
#             // dp[k][n] = 1 + min(max(broken[i], unbroken[i])), 1 <= i <= n
#             // find the smallest i such that broken[i] >= unbroken[i],
#             // which minimizes max(broken[i], unbroken[i]).
#             int l = 1;
#             int r = n + 1;
#             while (l < r) {
#               int m = l + (r - l) / 2;
#               int broken = dp(k - 1, m - 1);
#               int unbroken = dp(k, n - m);
#               if (broken >= unbroken)
#                 r = m;
#               else
#                 l = m + 1;
#             }
        
        def search(eggs, floors):
            if eggs <= 0:
                return 0
            elif eggs == 1:
                return floors
            elif floors <= 1:
                return floors
            elif dp[eggs][floors] != -1:
                return dp[eggs][floors]
            
            l, r = 1, floors+1
            while l < r:
                mid = l + (r-l) // 2
                broken = search(eggs-1, mid-1)
                intact = search(eggs, floors-mid)
                if broken < intact:
                    l = mid + 1
                else:
                    r = mid
            
            dp[eggs][floors] = 1 + search(eggs-1, l-1)
            return dp[eggs][floors]
        
        return search(eggs, floors)
