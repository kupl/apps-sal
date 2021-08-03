def beki(a, b):
    waru = 10**9 + 7
    ans = 1
    while(b > 0):
        if(1 & b):
            ans = ans * a % waru
        b >>= 1
        a = a * a % waru
    return ans


n, m = list(map(int, input().split()))
s = input()

ans = []
waru = 10**9 + 7

ru = [0] * (n + 1)
b = [1] * (n + 1)
for i in range(n):
    ru[i + 1] = ru[i] + int(s[i])
    b[i + 1] = (b[i] * 2) % waru
for i in range(m):
    l, r = list(map(int, input().split()))
    ko = ru[r] - ru[l - 1]
    ans.append((((b[ko] - 1)) * ((b[r + 1 - l - ko]))) % waru)

print("\n".join(list(map(str, ans))))
