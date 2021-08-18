class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        graph = {}
        u1, u2 = nums1[0], nums2[0]

        for n in range(len(nums1) - 1):
            u, v = nums1[n], nums1[n + 1]
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]

        for n in range(len(nums2) - 1):
            u, v = nums2[n], nums2[n + 1]
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]

        DP = {}
        MODN = 1000000007

        def solve(u):
            if u in DP:
                return DP[u]

            ans = u
            if u in graph:
                for v in graph[u]:
                    ans = max(ans, u + solve(v))
            DP[u] = ans
            return DP[u]

        ans = max(solve(u1), solve(u2)) % MODN
        return ans
