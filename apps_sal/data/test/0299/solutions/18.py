import math


def ost(a, b):
    if a % b != 0:
        return 1
    return 0


n = int(input())
data = list(map(int, input().split()))

ans = [0, 0, 0]

for i in range(n):
    ans[i % 3] += data[i]

anss = [ans[i] for i in range(3)]
anss.sort()
# print(anss,ans)
if ans[0] == anss[-1]:
    print("chest")
if ans[1] == anss[-1]:
    print("biceps")
if ans[2] == anss[-1]:
    print("back")
