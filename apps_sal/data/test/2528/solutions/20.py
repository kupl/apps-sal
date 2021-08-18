N = int(input())
A = list(map(int, input().split()))
cnt = 0
maxi = 0
for i in range(0, N):
    if A[i] != 0:
        cnt += 1
        if maxi < cnt:
            maxi = cnt

    else:
        cnt = 0
print(maxi)
