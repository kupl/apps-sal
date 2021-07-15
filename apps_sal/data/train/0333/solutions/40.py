import numpy as np
import heapq
from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        self.arr = arr

        # Hashing indices by values
        self.val2indx = {}
        for i,v in enumerate(arr):
            if not v in self.val2indx:  self.val2indx[v] = []
            self.val2indx[v].append(i)
        # print(\"val hash: \", self.val2indx)

        # Solutions memoization table
        self.solutions = [np.inf for i in range(len(arr))]
        self.solutions[-1] = 0
        self.visited = [False for i in range(len(arr))]
        
        node_q = deque()
        node_q.append((0, len(arr)-1))
        
        while node_q:
            # dist, indx = heapq.heappop(node_q)
            dist, indx = node_q.popleft()
            self.visited[indx] = True
            if dist > self.solutions[indx]: continue
                
            # Extracting edges
            next_indx, prev_indx = min(indx+1, len(self.arr)-1), max(indx-1, 0)
            indices = [i for i in self.val2indx[self.arr[indx]] if i != indx and i != prev_indx and i != next_indx and not self.visited[i]]    
            indices = [prev_indx, next_indx] + indices
            if not self.visited[prev_indx]: indices.append(prev_indx)
            if not self.visited[next_indx]: indices.append(next_indx)
            # exclude already visited nodes
            # indices = [i for i in indices if not self.visited[i]]
            # print(\"node:\", indx, \"edges\", indices)
                            
            # Update neighbour distances
            for j in indices:
                newdist = dist + 1
                if np.isinf(self.solutions[j]) or newdist < self.solutions[j] and not self.visited[j]:
                    self.solutions[j] = newdist
                    # heapq.heappush(node_q, (newdist, j))
                    node_q.append((newdist,j))
                    self.visited[j] = True
                    if j == 0: return newdist
        
        # print(\"solutions:\", self.solutions)
        return self.solutions[0]
            
            
        
        


# class Solution:
#     def getSolution(self, indx):
#         self.visitations[indx] = True
        
#         # Checking presence in hash table for the solution
#         if self.solutions[indx] is not None:
#             return self.solutions[indx]
#         else:
#             # min(indx-1, indx+1, indicees of val2indx[arr[indx]])
#             indices = [i for i in self.val2indx[self.arr[indx]] if i != indx]
#             indices = [min(indx+1, len(self.arr)-1), max(indx-1, 0)] + indices
#             indices = np.unique(indices)         
#             # exclude already visited states
#             indices = [i for i in indices if not self.visitations[i] or self.solutions[i] is not None]
#             print(indx, indices, self.solutions)
            
#             solutions = []
#             for i in indices:
#                 solutions.append(self.getSolution(i))
                
#                 # Just a shortcut to avoid unnecessary search
#                 if solutions[-1] == 1: 
#                     self.solutions[indx] = 2
#                     return self.solutions[indx]
            
#             if len(solutions) == 0: return np.inf
            
#             print(\"---\", indx ,\":\", solutions, np.min(solutions), indices)
#             self.solutions[indx] = 1 + np.min(solutions)
#             return self.solutions[indx]
    
#     def minJumps(self, arr: List[int]) -> int:
#         self.arr = arr

#         # Solutions memoization table
#         self.solutions = [None for i in range(len(arr))]
#         self.solutions[-1] = 0
#         self.solutions[-2] = 1
#         # self.visitations = [False for i in range(len(arr))]
#         # self.visitations[-2] = True
        
#         # Hashing indices by values
#         self.val2indx = {}
#         for i,v in enumerate(arr):
#             if not v in self.val2indx:  self.val2indx[v] = []
#             self.val2indx[v].append(i)
        
#         print(\"arr:\", arr)
#         print(\"val hash:\", self.val2indx)
#         # return 0
        
#         # Get solutions starting from the end
#         for i in range(len(arr)-2, -1, -1):
#             print(\"indx:\", i)
#             self.visitations = [False for j in range(len(arr))]
#             self.visitations[-2] = True
#             self.getSolution(indx=i)
        
        
#         print(\"solutions: \", self.solutions)
#         return self.solutions[0]
        
        

