import sys
n = int(input())
g1 = list(map(int, input().split()))
g2 = list(map(int, input().split()))
ans = 0
for i in range(1, 6):
    n1 = g1.count(i)
    n2 = g2.count(i)
    if abs(n1 - n2) % 2 != 0:
        print(-1)
        return
    ans += abs(n1 -n2)//2
print(ans//2)

