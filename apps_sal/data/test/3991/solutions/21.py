n = int(input())
arr = list(map(int, input().split()))
arr.sort()
mod = 10 ** 9 + 7
s = 0
ans = 0
m = 0
lAdd = 1
for i in range(n - 2, -1, -1):
    m += lAdd
    m %= mod
    lAdd *= 2
    lAdd %= mod
    s *= 2
    s %= mod
    s += arr[i + 1]
    s %= mod
    t = s - m * arr[i] % mod
    t += mod
    t %= mod
    ans += t
    ans %= mod
print(ans % mod)
