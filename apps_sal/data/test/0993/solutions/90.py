
N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] %= M
rui = [A[0]] * N
for i in range(1, N):
    rui[i] = (rui[i - 1] + A[i]) % M
rui.sort()
last = 0
cnt = 0
for i in range(1, N):
    if rui[i] != rui[i - 1]:
        if i - last >= 2:
            cnt += (i - last) * (i - last - 1) // 2
        last = i
if N - last >= 2:
    cnt += (N - last) * (N - last - 1) // 2
print(int(cnt) + rui.count(0))
