n = int(input())
A = list(map(int, input().split()))
tmp, cnt = 1, 0

for a in A:
    if a != tmp: cnt += 1
    else: tmp += 1

print(-1 if A.count(1) == 0 else cnt)
