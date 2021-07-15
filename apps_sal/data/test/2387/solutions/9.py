#abc167_e

n = int(input())

pos = []
neg = []

for _ in range(n):
    s = input()
    low_pos = 0
    increase= 0
    for v in s:
        if v=="(":
            increase += 1
        else:
            increase -= 1
            low_pos = min(low_pos, increase)
    
    if increase >= 0:
        pos.append((low_pos, increase))
    else:
        #reverse left from right
        low_pos, increase =  low_pos - increase, -increase        
        neg.append((low_pos, increase))
    
pos.sort()
pos.reverse() #lowが高い順にする.
neg.sort()
neg.reverse() #lowが高い順にする.

now_pos = 0
for low_pos, increase in pos:
    if now_pos + low_pos < 0:
        print("No")  #impossible
        return
    else:
        now_pos += increase

right_pos = 0       
for low_pos, increase in neg:
    if right_pos + low_pos < 0:
        print("No")  #impossible
        return
    else:
        right_pos += increase

if right_pos != now_pos:
    print("No")
    return
else:
    print("Yes")
