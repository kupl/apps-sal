N = int(input())
A = list(map(int, input().split()))
A.sort()
check = [0] * N
for idx in range(N % 2, N, 2):
    check[idx] = idx + 1
    check[idx + 1] = idx + 1
ans = 0
if check == A:
    if N % 2 == 0:
        ans = 2 ** (N // 2) % (10 ** 9 + 7)
    elif N % 2 != 0:
        ans = 2 ** ((N - 1) // 2) % (10 ** 9 + 7)
print(ans)
