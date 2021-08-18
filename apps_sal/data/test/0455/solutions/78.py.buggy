import bisect
import sys
input = sys.stdin.readline


N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
r = (XY[0][0] + XY[0][1]) % 2
for i in range(N):
    if r != (XY[i][0] + XY[i][1]) % 2:
        print((-1))
        return

sumtwo = []
mul = 2
for i in range(31):
    sumtwo.append(mul - 1)
    mul *= 2


maxtwo = 0
i_two = 0
for i in range(N):
    if maxtwo < abs(XY[i][0]) + abs(XY[i][1]):
        i_two = bisect.bisect_left(sumtwo, abs(XY[i][0]) + abs(XY[i][1]))
        maxtwo = sumtwo[i_two]
ans = [2**i for i in range(i_two + 1)]
if r == 0:
    ans = [1] + ans
    i_two += 1
print((i_two + 1))
print((*ans))
ans.reverse()

for i in range(N):
    ans2 = []
    nowx, nowy = XY[i]
    for j in range(i_two + 1):
        if abs(nowx) < abs(nowy):
            if nowy < 0:
                ans2.append("D")
                nowy += ans[j]
            else:
                ans2.append("U")
                nowy -= ans[j]
        else:
            if nowx < 0:
                ans2.append("L")
                nowx += ans[j]
            else:
                ans2.append("R")
                nowx -= ans[j]
    ans2.reverse()
    print(("".join(ans2)))
