class Solution:
    def minJumps(self, arr: List[int]) -> int:
        q = deque([[0, 0]])
        d = defaultdict(list)
        vis = set([0])
        for i,val in enumerate(arr):
            d[val].append(i)
        
        while q:
            idx, steps = q.popleft()
            if idx == len(arr)-1:
                return steps
            for i in d.pop(arr[idx], [])+[idx+1, idx-1][::-1]:
                if i not in vis and i >= 0:
                    vis.add(i)
                    q.append([i, steps + 1])
