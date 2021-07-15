class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = []
        if arr[start] == 0:
            return True
        currNodes = [start]
        
        while len(visited) < len(arr):
            temp = []
            for i in currNodes:
                visited += [i]
                candidate1 = i+arr[i]
                candidate2 = i-arr[i]
                if candidate1 < len(arr) and candidate1 not in visited:
                    if arr[candidate1] == 0:
                        return True
                    temp += [candidate1]
                if candidate2 >= 0 and candidate2 not in visited:
                    if arr[candidate2] == 0:
                        return True
                    temp += [candidate2]
            if len(temp) == 0:
                break
            currNodes = temp
        return False
                    

