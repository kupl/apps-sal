class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == 1:
            if m == 0:
                return 0
            elif m == 1:
                return 1
            else:
                return -1
        
        if len(arr) == m:
            return m
        
        freq_indices = []
        last_freq = -1
        goal_freq = 0
        arr = [el - 1 for el in arr]
        left = [None] * len(arr)
        right = [None] * len(arr)
        
        idx = 0
        while idx < len(arr):
            change = arr[idx]
            if change == 0:
                left_end = change
                right_end = right[change + 1]
                left_size = 0
                if right_end is None:
                    right_end = change
                    right_size = 0
                else:
                    right_size = right_end - change
                
                right[change] = right_end
                left[right_end] = left_end
                
                if right_size == m:
                    goal_freq -= 1
                
                new_size = right_end - left_end + 1
                if new_size == m:
                    goal_freq += 1
                
                # print(new_size, goal_freq)
                if goal_freq > 0:
                    last_freq = idx
                    
            elif change == len(arr) - 1:
                right_end = len(arr) - 1
                left_end = left[change - 1]
                right_size = 0
                if left_end is None:
                    left_end = change
                    left_size = 0
                else:
                    left_size = change - left_end
                
                left[change] = left_end
                right[left_end] = right_end
                
                if left_size == m:
                    goal_freq -= 1
                
                new_size = right_end - left_end + 1
                if new_size == m:
                    goal_freq += 1
                
                if goal_freq:
                    last_freq = idx
                    
            else:
                left_end = left[change - 1]
                right_end = right[change + 1]
                if right_end is None:
                    right_end = change
                    right_size = 0
                else:
                    right_size = right_end - change
                    
                if left_end is None:
                    left_end = change
                    left_size = 0
                else:
                    left_size = change - left_end
                
                right[left_end] = right_end
                left[right_end] = left_end
                
                if right_size == m:
                    goal_freq -= 1
                    
                if left_size == m:
                    goal_freq -= 1
                
                
                new_size = right_end - left_end + 1
                if new_size == m:
                    goal_freq += 1
                
                if goal_freq:
                    last_freq = idx
            idx += 1
        
        if last_freq != -1:
            return last_freq + 1
        return -1
