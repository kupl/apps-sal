def rps(a, b):
    if a == 'R' and b == 'S':
        return a
    if a == 'P' and b == 'R':
        return a
    if a == 'S' and b == 'P':
        return a
    if a == b:
        return a
    return b


n, k = map(int, input().split())
s = list(input())
for _ in range(k):
    t = list(s) * 2
    s = ''
    for i in range(0, n * 2, 2):
        s += rps(t[i], t[i + 1])
print(s[0])
