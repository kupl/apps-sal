class Solution:

    def minJumps(self, arr: List[int]) -> int:
        v_jumped = set()
        v_idx = collections.defaultdict(list)
        for (i, v) in enumerate(arr):
            v_idx[v].append(i)
        q = [0]
        seen_idx = {0}
        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                i = q.pop(0)
                if i == len(arr) - 1:
                    return step
                if arr[i] not in v_jumped:
                    v_jumped.add(arr[i])
                    for j in v_idx[arr[i]]:
                        if j not in seen_idx:
                            seen_idx.add(j)
                            q.append(j)
                if i + 1 < len(arr) and i + 1 not in seen_idx:
                    seen_idx.add(i + 1)
                    q.append(i + 1)
                if i - 1 >= 0 and i - 1 not in seen_idx:
                    seen_idx.add(i - 1)
                    q.append(i - 1)
            step += 1
        return -1
