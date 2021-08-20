class Solution:

    def minJumps(self, nums):
        neighbors = defaultdict(list)
        _ = [neighbors[num].append(i) for (i, num) in enumerate(nums)]
        q = deque([(0, 0)])
        (num_seen, pos_seen) = (set(), set())
        while q:
            (pos, step) = q.popleft()
            if pos == len(nums) - 1:
                return step
            num = nums[pos]
            pos_seen.add(pos)
            for p in [pos - 1, pos + 1] + neighbors[num] * (num not in num_seen):
                if p in pos_seen or not 0 <= p < len(nums):
                    continue
                q.append((p, step + 1))
            num_seen.add(num)
