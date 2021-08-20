def f(s, t):
    a = [0, []]
    for i in range(len(s)):
        if s[i] != t[i]:
            a[0] += 1
            a[1].append(i + 1)
    return a


(n, m) = list(map(int, input().split()))
s = input()
t = input()
ans = 2000
a = []
for i in range(m - n + 1):
    if f(s, t[i:i + n])[0] < ans:
        (ans, a) = f(s, t[i:i + n])
print(ans)
for i in a:
    print(i, end=' ')
