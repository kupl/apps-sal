class Solution:
    def minDays(self, n: int) -> int:
        step = 0
        seen1 = set([0])
        seen2 = set([n])
        q1 = collections.deque([0])
        q2 = collections.deque([n])
        if n == 1:
            return 1
        while q1 and q2:
            for _ in range(len(q1)):
                node = q1.popleft()
                if node in seen2:
                    return step
                if node * 3 < n and node * 3 not in seen1:
                    q1.append(node * 3)
                    seen1.add(node * 3)
                if node * 2 < n and node * 2 not in seen1:
                    q1.append(node * 2)
                    seen1.add(node * 2)
                if node + 1 not in seen1:
                    q1.append(node + 1)
                    seen1.add(node + 1)
            # print(q1, seen1, step)
            step += 1
            for _ in range(len(q2)):
                node = q2.popleft()
                if node in seen1:
                    return step
                if node % 3 == 0 and node // 3 not in seen2:
                    q2.append(node // 3)
                    seen2.add(node // 3)
                if node % 2 == 0 and node // 2 not in seen2:
                    q2.append(node // 2)
                    seen2.add(node // 2)
                if node - 1 not in seen2:
                    q2.append(node - 1)
                    seen2.add(node - 1)
            step += 1
        return -1

