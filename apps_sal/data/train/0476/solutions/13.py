class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         c=0
#         cnt=[]
#         for i in range(len(position)):
#             temp=[]
#             while(position[i]!=target):
#                 temp.append(position[i])
#                 position[i]=position[i]+speed[i]
#             temp.append(12)
#             cnt.append(temp)
#         for i in range(len(cnt)):
#             for j in range(i+1,len(cnt)):
#                 for k in cnt[i]:
#                     if k in cnt[j]:
#                         if(cnt[i].index(k)==cnt[j].index(k)):
#                             c=c+1
            
        
#         print(cnt)
            cars = sorted(zip(position, speed))
            print(cars)
            times = [float(target - p) / s for p, s in cars]
            print(times)
            ans = 0
            while len(times) > 1:
                lead = times.pop()
                if lead < times[-1]: ans += 1  # if lead arrives sooner, it can't be caught
                else: times[-1] = lead # else, fleet arrives at later time 'lead'

            return ans + bool(times) # remaining car is fleet (if it exists)
