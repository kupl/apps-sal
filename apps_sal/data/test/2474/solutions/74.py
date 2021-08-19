mod = 10 ** 9 + 7
n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
ans = 0
if n == 1:
    print(2 * arr[0] % mod)
else:
    table = [1]
    for _ in range(n):
        tmp = table[-1] * 2
        tmp %= mod
        table.append(tmp)
    for i in range(n):
        if i == n - 1:
            ans += table[i - 1] * (n - i + 1) * arr[i] % mod
        else:
            ans += table[i] * (n - i + 1) * table[n - i - 2] * arr[i] % mod
    print(ans * table[n] % mod)
