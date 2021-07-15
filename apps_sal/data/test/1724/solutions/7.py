3

def readln(): return tuple(map(int, input().split()))

n, = readln()
a = readln()
s = [0] * (n + 1)
sm = [0] * (n + 1)
m = list(input())
for i in range(n):
    s[i + 1] = s[i] + a[i]
    sm[i + 1] = sm[i] + (a[i] if m[i] == '1' else 0)
ans = sm[n]
for i in range(n - 1, -1, -1):
    if m[i] == '1':
        ans = max(ans, s[i] + sm[n] - sm[i + 1])
print(ans)

