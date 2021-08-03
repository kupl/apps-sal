class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        adj = {i: [] for i in range(len(arr))}
        target = {}

        for idx, jump in enumerate(arr):
            choice_a = idx - jump
            choice_b = idx + jump
            if choice_a >= 0 and choice_a < len(arr):
                adj[idx].append(choice_a)
            if choice_b > 0 and choice_b < len(arr):
                adj[idx].append(choice_b)
            if jump == 0:
                target[idx] = True
            else:
                target[idx] = False
        q = deque([start])
        visited = []
        while q:
            cur = q[0]
            q.popleft()
            visited.append(cur)
            for neighbor in adj[cur]:
                if target[neighbor]:
                    return True
                if neighbor not in visited:
                    q.append(neighbor)
        return False
