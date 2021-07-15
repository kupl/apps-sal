n = int(input())
A = list(map(int,input().split()))

if 1 not in A:
    print(-1)
    return

chk = 1
cnt = 0
for i in range(n):
    if A[i] == chk:
        cnt += 1
        chk += 1

print(len(A) - cnt)
