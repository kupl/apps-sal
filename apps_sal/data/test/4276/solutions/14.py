# coding: utf-8

num, time = map(int, input().split())
count = 0
ans = 10000
for i in range(num):
    cost, tm = map(int, input().split())
    if tm <= time:
        if cost < ans:
            ans = cost
            max = ans
            count = 1
if count == 0:
    print("TLE")
else:
    print(ans)
