class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        '''
        ex 1
        arr = [1,2,3,4,5,10,6,7,8,9], k = 5
        (2,8), (1,9), (3,7), (4,6), (5,10)
        return True

        ex 2
        arr = [1,2,3,4,5,6], k = 7
        (1,6), (2,5), (3,4)
        return True

        ex 3
        arr = [1,2,3,4,5,6], k = 10
        [1,2,3,5]
        (4,6), 
        return False

        ex 4
        arr = [-10,10], k = 2
        return True

        ex 5
        arr = [-1,1,-2,2,-3,3,-4,4], k = 3
        (-1,-2), (1,2), (-3,3), (-4,4)
        return True

        idea 1
        greedy, two pointers
        time - O(nlogn), space - O(n)
        '''
        arr_mod = [num % k for num in arr]
        arr_mod.sort()
        n = len(arr_mod)
        left, right = 0, n - 1
        while left < n and arr_mod[left] == 0:
            left += 1
        if left % 2 != 0:
            return False
        while left < right:
            if arr_mod[left] + arr_mod[right] == k:
                left += 1
                right -= 1
            else:
                return False
        return True
