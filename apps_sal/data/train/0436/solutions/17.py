from math import log,ceil

class Solution:
    def minDays( self, n: int) -> int:
        def one_day(apples):
            if apples%2==0 and apples%3!=0:
                return (apples/2,apples-1)
            elif apples%3==0 and apples%2!=0:
                return (apples/3,apples-1)
            elif apples%3==0 and apples%2==0:
                return (apples/3,apples/2)
            elif apples%3!=0 and apples%2!=0:
                return (apples-1,)


        poses=[(n,0)]#(#apples remained,days passed)
        min_apples=min([pos[0] for pos in poses])

        while min_apples!=0:
            new_poses=[]
            for pos in poses:
                apples=pos[0]
                days=pos[1]
                new_pos=[(new_apples,days+1)for new_apples in one_day(apples)]
                if min([pos[0] for pos in new_pos])==0:
                    return sorted(new_pos,key=lambda x:x[0])[0][1]
                new_poses+=new_pos
            min_apples=min([pos[0] for pos in new_poses])
            poses=sorted(list(set(new_poses)))
            # print(poses)

        days=sorted(poses,key=lambda x:x[0])[0][1]

        return days
