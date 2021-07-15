class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        
        steps = n
        a1 = [[1, n]]
        a2 = [n]
        if m == n:
            return steps
        
        while steps > 0:
            steps -= 1
            i = arr[steps]
            
            l = 0
            r = len(a1) - 1
            
            while l <= r:
                mid = (l + r) // 2
                if a1[mid][0] > i:
                    r = mid - 1
                elif a1[mid][1] < i:
                    l = mid + 1
                else:
                    left = [a1[mid][0], i - 1]
                    right = [i + 1, a1[mid][1]]
                    
                    if left[0] > left[1]:
                        if right[0] > right[1]:
                            a1.pop(mid)
                            a2.pop(mid)
                            break
                        else:
                            a1[mid] = right
                            a2[mid] = right[1] - right[0] + 1
                            if a2[mid] == m:
                                return steps
                    else:
                        if right[0] > right[1]:
                            a1[mid] = left
                            a2[mid] = left[1] - left[0] + 1
                            if a2[mid] == m:
                                return steps
                        else:
                            a1[mid] = right
                            a2[mid] = right[1] - right[0] + 1
                            a1.insert(mid, left)
                            a2.insert(mid, left[1] - left[0] + 1)
                            if a2[mid] == m or a2[mid + 1] == m:
                                return steps
        return -1
