n = int(input())
a = list(map(int, input().split()))

rate = [0] * 8
s = 0

for i in a:
    if i < 400:
        rate[0] = 1
    elif 400 <= i < 800:
        rate[1] = 1
    elif 800 <= i < 1200:
        rate[2] = 1
    elif 1200 <= i < 1600:
        rate[3] = 1
    elif 1600 <= i < 2000:
        rate[4] = 1
    elif 2000 <= i < 2400:
        rate[5] = 1
    elif 2400 <= i < 2800: 
        rate[6] = 1
    elif 2800 <= i < 3200:
        rate[7] = 1
    elif 3200 <= i:
        s += 1



    
ans1 = 8-rate.count(0)
ans2 = ans1+s
if ans1 == 0 and s != 0:
    ans1 = 1


print(ans1, ans2)
