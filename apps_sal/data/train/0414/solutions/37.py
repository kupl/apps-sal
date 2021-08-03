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
        if k >= len(arr) - 1:
            return max(arr)

        left_wins = 0

        while (left_wins != k):
            if arr[0] > arr[1]:
                left_wins += 1
                arr.append(arr[1])
                arr.pop(1)
            else:
                left_wins = 1
                arr.append(arr[0])
                arr.pop(0)

        return arr[0]
