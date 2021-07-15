n = int(input())
a = list(map(int, input().split()))
r = 0
ans = 0
s = 0
xor = 0

for i in range(n):
    while r < n:
        if xor ^ a[r] == s + a[r]:
            xor = xor ^ a[r]
            s += a[r]
            r += 1
            ans += (r-i)
        else:
            xor = xor ^ a[i]
            s -= a[i]
            break

print(ans)

