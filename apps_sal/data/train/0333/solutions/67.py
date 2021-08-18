class Solution:
    def minJumps(self, arr: List[int]) -> int:
        record = collections.defaultdict(list)
        for i, v in enumerate(arr):
            record[v].append(i)
        nums = set()
        pos_met = set()
        q = collections.deque([(0, 0)])
        while q:
            pos, step = q.popleft()
            if pos == len(arr) - 1:
                return step
            num = arr[pos]
            pos_met.add(pos)
            temp = [pos - 1, pos + 1]
            if num not in nums:
                for j in record[num]:
                    temp += [j]
            nums.add(num)
            for i in temp:
                if 0 <= i < len(arr) and i not in pos_met:
                    q.append([i, step + 1])
