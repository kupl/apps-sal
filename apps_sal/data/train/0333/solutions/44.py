class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = {}
        seen = set()
        queue = deque([(0, 0)])

        for i, num in enumerate(arr):
            if i == 0 or i == len(arr) - 1 or (arr[i - 1] != arr[i] or arr[i + 1] != arr[i]):
                d[num] = d.get(num, []) + [i]

        while queue:
            next_idx, steps = queue.popleft()

            if next_idx == len(arr) - 1:
                return steps

            if next_idx + 1 <= len(arr) and next_idx + 1 not in seen:
                queue.append((next_idx + 1, steps + 1))
                seen.add(next_idx + 1)

            if next_idx - 1 >= 0 and next_idx - 1 not in seen:
                queue.append((next_idx - 1, steps + 1))
                seen.add(next_idx - 1)

            for i in d[arr[next_idx]][::-1]:
                if i != next_idx and i not in seen:
                    queue.append((i, steps + 1))
                    seen.add(i)

        return -1
