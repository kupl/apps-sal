from itertools import combinations as C

N = int(input())
d = list(map(int, input().split()))

D = list(C(d, 2))

ans = 0

for i in D:
    ans += i[0] * i[1]

print(ans)
