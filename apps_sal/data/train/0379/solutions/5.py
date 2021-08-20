class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        indeg = defaultdict(int)
        g = defaultdict(list)
        for i in range(len(nums1) - 1):
            g[nums1[i]].append(nums1[i + 1])
            indeg[nums1[i + 1]] += 1
        for i in range(len(nums2) - 1):
            g[nums2[i]].append(nums2[i + 1])
            indeg[nums2[i + 1]] += 1
        q = deque()
        ans = 0
        dists = defaultdict(int)
        for num in g:
            if indeg[num] == 0:
                q.append((num, num))
                dists[num] = num
        while q:
            (num, score) = q.popleft()
            ans = max(ans, score)
            for nei in g[num]:
                indeg[nei] -= 1
                dists[nei] = max(dists[nei], score)
                if indeg[nei] == 0:
                    q.append((nei, nei + dists[nei]))
        return ans % (10 ** 9 + 7)
