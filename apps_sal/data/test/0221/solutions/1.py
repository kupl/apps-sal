#import sys
#sys.stdin = open("in.txt", "r")

n, k = map(int, input().split())
one = k * 2 + 1

ans = 0
if n % one == 0: ans = n // one
else: ans = n // one + 1
print(ans)
cnt = 1
arr = []
t = one // 2 + 1
minus = 0
while cnt <= ans:
    if t > n:
        minus = t - n
    arr += [t]
    #print("%d" % t, end=" ")
    t += one
    cnt += 1

for s in arr:
    print("%d" % (s - minus), end=" ")
