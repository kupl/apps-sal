class Solution:

    def minJumps(self, arr):
        nei = collections.defaultdict(list)
        _ = [nei[x].append(i) for (i, x) in enumerate(arr)]
        frontier = collections.deque([(0, 0)])
        (num_met, pos_met) = (set(), set())
        while frontier:
            (pos, step) = frontier.popleft()
            if pos == len(arr) - 1:
                return step
            num = arr[pos]
            pos_met.add(pos)
            nexts = [pos - 1, pos + 1] + nei[num] if num not in num_met else [pos - 1, pos + 1]
            for p in nexts:
                if p in pos_met or not 0 <= p < len(arr):
                    continue
                frontier.append((p, step + 1))
            num_met.add(num)
