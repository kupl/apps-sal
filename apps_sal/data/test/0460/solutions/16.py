# written by sak
#
#	sk<3
#
# powered by codechef

import math
z = input()
z = z.split(' ')
p = int(z[0])
x = int(z[1])
y = int(z[2])

i = int(math.floor(x / 50))
i = i % 475
flag = 0
for j in range(0, 25):
    i = (i * 96 + 42) % 475
    # print(26+i)
    if((26 + i) == p):
        print("0")
        flag = 1
        break
if(flag != 1):
    ans = 0
    while 1:
        curr = x + 100 * ans
        while(curr >= y):
            i = int(math.floor(curr / 50))
            i = i % 475
            win = {}
            for j in range(0, 25):
                i = (i * 96 + 42) % 475
                if((26 + i) == p):
                    print(ans)
                    flag = 1
                    break
            curr -= 50
            if(flag == 1):
                break
        ans += 1
        if(flag == 1):
            break
