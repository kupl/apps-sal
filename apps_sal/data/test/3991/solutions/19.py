n = int(input())
arr = sorted(list(map(int, input().split())))
res = 0
mod = 1000000007
acc = 0
arr = [arr[i+1] - arr[i] for i in range(n-1)]
n -= 1
s = sum(arr)
for i in range((n+1)//2):
    acc += s
    res += acc * pow(2, n-i-1, mod) % mod
    if not i*2+1 == n:
        res += acc * pow(2, i, mod) % mod
    res %= mod
    s -= arr[i] + arr[n-i-1]
print(res)
