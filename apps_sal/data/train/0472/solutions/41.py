class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
#         n = len(arr);
        
#         visited = [False for _ in range(n)];
        
#         def helper(i):
#             if  i < 0 or i > n-1 or visited[i]:
#                 return False;
#             if arr[i] == 0:
#                 return True;
            
#             visited[i] = True;
            
#             right = helper(i+arr[i]);
#             left  = helper(i-arr[i]);
            
#             visited[i] = False;
            
#             if right or left:
#                 return True;
#             return False;
        
#         return helper(start);

        if not arr:
            return False;
        if arr[start] == 0:
            return True;
        queue = [start];
        n = len(arr);
        visited = [False for _ in range(n)];
        
        while queue:
            index = queue.pop(0);
            visited[index] = True;
            newIndices = [index - arr[index], index + arr[index]];
            
            for i in newIndices:
                if i>=0 and i<n and not visited[i]:
                    queue.append(i);
                    if arr[i] == 0:
                        return True;
        return False;
            
            
        

