class Solution:
    def minJumps(self, arr: List[int]) -> int:
        from collections import deque, defaultdict
        d = defaultdict(set)
        q = deque([0])
        res = 0
        last = len(arr) - 1
        for i in range(len(arr)):
            d[arr[i]].add(i)
        d[arr[0]].remove(0)
        print(d)
        while q:
            for i in range(len(q)):
                e = q.popleft()
                if e == last:
                    return res
                if e - 1 >= 0 and e - 1 in d[arr[e - 1]]:
                    q.append(e - 1)
                    d[arr[e - 1]].remove(e - 1)
                if e + 1 <= last and e + 1 in d[arr[e + 1]]:
                    q.append(e + 1)
                    d[arr[e + 1]].remove(e + 1)
                for n in d[arr[e]]:
                    q.append(n)
                d[arr[e]] = []
            res += 1
        return res
