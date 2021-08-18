import collections


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        suma = [0]

        for item in A:
            suma.append(suma[-1] + item)

        ansr = len(A) + 1

        queue = collections.deque()

        for i in range(len(suma)):

            while queue and suma[i] - suma[queue[0]] >= K:
                ansr = min(ansr, i - queue[0])
                queue.popleft()

            while queue and suma[i] <= suma[queue[-1]]:
                queue.pop()

            queue.append(i)

        if ansr == len(A) + 1:
            return -1
        else:
            return ansr
