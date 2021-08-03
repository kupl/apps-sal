class Solution:
    def minJumps(self, arr: List[int]) -> int:

        seen = {0}
        q = [0]
        goal = len(arr) - 1

        linked = collections.defaultdict(list)
        for idx, x in enumerate(arr):
            linked[x].append(idx)

        q_back = [goal]
        q = [0]
        levels = -1

        while q:
            levels += 1
            q_len = len(q)
            for _ in range(q_len):
                idx = q.pop(0)

                if idx == goal:

                    return levels

                if idx + 1 not in seen:
                    q.append(idx + 1)
                    seen.add(idx + 1)

                if idx > 0 and idx - 1 not in seen:
                    q.append(idx - 1)
                    seen.add(idx - 1)

                for link in linked[arr[idx]]:
                    if link not in seen:
                        q.append(link)
                        seen.add(link)

                del linked[arr[idx]]
