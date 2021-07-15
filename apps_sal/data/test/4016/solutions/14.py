n, k = list(map(int, input().split()))
t = list(input())
for i in range(1, n + 1):
    if t[i:] == t[:n - i]:
        s = t[:i] * k
        s += t[i:]
        break
print(''.join(s))

