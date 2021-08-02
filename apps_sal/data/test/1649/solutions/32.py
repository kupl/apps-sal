A = list(map(int, input().split()))
for i in range(2**4):
    cnt = 0
    for j in range(4):
        if i >> j & 1:
            cnt += A[j]
        if cnt * 2 == sum(A):
            print("Yes")
            return
print("No")
