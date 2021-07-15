import sys
a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))
times1 = [b + a*i for i in range(100)]
for time2 in [d + c*i for i in range(100)]:
        if time2 in times1:
                print(time2)
                return
print(-1)

