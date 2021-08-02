N, M = list(map(int, input().split()))
A = [int(input()) for _ in range(M)]

step = [0] * (N + 1)
last = -1
for a in A:
    if a == last + 1 or a == last - 1:
        print((0))
        return
    step[a] = 1
    last = a

ans = [0] + [1] + [0] * N

chk = 0
for i in range(1, N + 1):
    if step[i] == 0 and chk <= 0:
        ans[i + 1] = ans[i] + ans[i - 1]
        chk = 0
    elif step[i] == 1:
        ans[i + 1] = ans[i]
        chk = 2
    elif step[i] == 0 and chk > 0:
        ans[i + 1] = ans[i]
        chk -= 1

print((ans[-1] % (10**9 + 7)))
