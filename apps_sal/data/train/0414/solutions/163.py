class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        '''
        - arr length always <= 2
        - distinct elements
        
        
        1. left_wins = 0
        2. Compare first two elements
        3a. if left >, increment left_wins, move second element to back
        3b. else, set left_wins = 1, move first element back, remove it
        4. return if left_wins == k
        
        O(k*N*N) Time  O(1) Space
        
        
        [6,3,4,5,7] k = 3
        
        len(arr)-k
        '''
        curr = arr[0]
        wins = 0
        
        for i in range(1, len(arr)):
            if curr > arr[i]:
                wins += 1
            else:
                curr = arr[i]
                wins = 1
            if wins == k:
                return curr
            
        return curr
        

