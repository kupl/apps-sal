class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # U could do this in BFS, dont over thinking!
        # Start from 0,0 (position, step)
        # Record all the numbers and positions stepped on
        # Once u stepped on certain number, u will try out all the candidates
        # So no twice on the same number
        # And each time check within valid range
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
                # Here, even though u make sure the num is not stepped on
                # Remember to check if the position is stepped on!
                if 0 <= i < len(arr) and i not in pos_met:
                    q.append([i, step + 1])
