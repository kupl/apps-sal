class Solution:
    def minOperations(self, n: int) -> int:
        
        def isAllEqual(array):
            for i in range(len(array[1:])):
                if array[i] != array[0]:
                    return False
            
            return True
        
        # generate array; where array[i] = 2i + 1
        arr = [((2 * x)+1) for x in range(n)]
        
        # choose x and y, arr[x]-=1 arr[y]-=1
        # generate all pairs
        count = 0
        x = 0
        y = len(arr)-1
        
        while (x < y):
            diff = int((arr[y]-arr[x])/2)
            arr[x] += diff
            arr[y] -= diff
            count += diff
            x += 1
            y -= 1
        
        return count

