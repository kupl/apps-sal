N = int(input())
A = list(map(int, input().split()))
tmp = [0 for _ in range(10 ** 5)]
for i in range(N):
    tmp[A[i] - 1] += 1
ans = N
flag = False
for i in range(10 ** 5):
    if tmp[i] == 0:
        continue
    elif tmp[i] % 2 == 1:
        ans -= tmp[i] - 1
    elif flag:
        ans -= tmp[i] - 2
        flag = False
    else:
        ans -= tmp[i]
        flag = True
print(ans)
