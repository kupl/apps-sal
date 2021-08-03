from operator import *
N = int(input())
AB = [list(map(int, input().split())) for n in range(N)]
AB = sorted(AB, key=itemgetter(1))
ans = "Yes"
T = 0

for a, b in AB:
    T += a
    if b < T:
        ans = "No"

print(ans)
