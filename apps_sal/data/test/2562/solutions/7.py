import sys
useless = sys.stdin.readline()
a = list(map(int, sys.stdin.readline().split()))
n = 1000001
mod = 1000000007
cnt = [0] * n
for i in a:
    cnt[i] += 1
arr = [0] * n
ans = 0
for i in range(n - 1, 1, -1):
    j = sum(cnt[i::i])
    if j > 0:
        arr[i] = (j * pow(2, j - 1, mod) - sum(arr[i::i])) % mod
        ans = (ans + i * arr[i]) % mod
sys.stdout.write(str(ans))
