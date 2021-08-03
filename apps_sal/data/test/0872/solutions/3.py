import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

ki = 0
gu = 0

for a in A:
    if a % 2 == 0:
        gu = 1
    else:
        ki = 1

if ki == 1 and gu == 1:
    print(*sorted(A))
else:
    print(*A)
