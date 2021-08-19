import numpy as np
import heapq
from collections import deque


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        self.arr = arr
        self.val2indx = {}
        for (i, v) in enumerate(arr):
            if not v in self.val2indx:
                self.val2indx[v] = []
            self.val2indx[v].append(i)
        self.solutions = [np.inf for i in range(len(arr))]
        self.solutions[-1] = 0
        self.visited = [False for i in range(len(arr))]
        node_q = deque()
        node_q.append((0, len(arr) - 1))
        while node_q:
            (dist, indx) = node_q.popleft()
            self.visited[indx] = True
            if dist > self.solutions[indx]:
                continue
            (next_indx, prev_indx) = (min(indx + 1, len(self.arr) - 1), max(indx - 1, 0))
            indices = [i for i in self.val2indx[self.arr[indx]] if i != indx and i != prev_indx and (i != next_indx) and (not self.visited[i])]
            indices = [prev_indx, next_indx] + indices
            if not self.visited[prev_indx]:
                indices.append(prev_indx)
            if not self.visited[next_indx]:
                indices.append(next_indx)
            for j in indices:
                newdist = dist + 1
                if np.isinf(self.solutions[j]) or (newdist < self.solutions[j] and (not self.visited[j])):
                    self.solutions[j] = newdist
                    node_q.append((newdist, j))
                    self.visited[j] = True
                    if j == 0:
                        return newdist
        return self.solutions[0]
