class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        link = collections.defaultdict(list)
        for i, x in enumerate(arr):
            link[x].append(i)
        lvl = 0
        num_met, pos_met = set(), set()
        # dp = [-1]*len(arr)
        queue = collections.deque([0])  # put index
        while queue:
            L = len(queue)
            for i in range(L):
                x = queue.popleft()
                if x == len(arr) - 1:
                    return lvl
                num = arr[x]
                pos_met.add(x)

                for k in [x - 1, x + 1] + link[num] * (num not in num_met):  # 取交集
                    if k in pos_met or not 0 <= k < len(arr):
                        continue
                    queue.append(k)
                num_met.add(num)
            lvl += 1
        return 0
