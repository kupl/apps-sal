import math
test = int(input())
for t in range(test):
    tt = 0
    pp = 0
    cc = ""
    ss = ""
    dd = 1
    cnttt = 0
    # write yoour code here
    x = int(input())
    a = x
    cnt = 0
    while(a != 0):
        a = a // 10
        cnt += 1
    a = x % 10
    ans = (a - 1) * 10 + cnt * (cnt + 1) // 2
    print(ans)
