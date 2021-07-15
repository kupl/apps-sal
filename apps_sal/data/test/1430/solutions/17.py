N, K = map(int, input().split())
S = input()

arr = []

if S[0] == '0':
    arr.append(0)

cnt = 0
for i in range(N - 1):
    if S[i] == S[i + 1]:
        cnt += 1
    else:
        arr.append(cnt + 1)
        cnt = 0
arr.append(cnt + 1)

if S[-1] == '0':
    arr.append(0)

res = 0
s = 0
i = 0
while i < 2 * K + 1 and i < len(arr):
    s += arr[i]
    i += 1

res = s

while i < len(arr) - 1:
    s += arr[i] + arr[i + 1] - arr[i - 2 * K - 1] - arr[i - 2 * K]
    res = max(s, res)

    i += 2

print(res)
