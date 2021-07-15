class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        max_distance = 0
        for i, seat in enumerate(seats):
            if seat == 1:
                pass
            
            else:
                left = right = i
                location = [0, 0]
                while 0 <= left < len(seats):
                    if seats[left] != 1:
                        location[0] += 1
                        left -= 1
                    else:
                        break
                        
                
                while 0 <= right < len(seats):
                    if seats[right] != 1:
                        location[1] += 1
                        right += 1
                    else:
                        break
                        
                if i == 0 or i == len(seats) - 1:
                    distance = max(location[0], location[1])
                else:
                    distance = min(location[0], location[1])
                        
                if distance > max_distance:
                    max_distance = distance
                        
                
                
                
        print(max_distance)
        return max_distance
                    

