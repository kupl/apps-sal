class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = list(range(len(arr)))
        sz = [0] * len(arr)
        steps = set()

        def find(x):
            while x != uf[x]:
                x = uf[x]
            return x

        def union(p, q):
            (pid, qid) = (find(p), find(q))
            if pid == qid:
                return
            if sz[pid] == m and pid in steps:
                steps.remove(pid)
            if sz[qid] == m and qid in steps:
                steps.remove(qid)
            if sz[pid] < sz[qid]:
                uf[pid] = qid
                sz[qid] += sz[pid]
            else:
                uf[qid] = pid
                sz[pid] += sz[qid]
        last_step = -1
        for i in range(len(arr)):
            idx = arr[i] - 1
            sz[idx] = 1
            if idx - 1 >= 0 and sz[idx - 1]:
                union(idx - 1, idx)
            if idx + 1 < len(arr) and sz[idx + 1]:
                union(idx + 1, idx)
            if sz[find(idx)] == m:
                steps.add(find(idx))
            if steps:
                last_step = i + 1
        return last_step
