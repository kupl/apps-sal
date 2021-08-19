(n, k) = list(map(int, input().split()))
t = input()
for i in range(n - 1, -1, -1):
    if t[:i] == t[n - i:]:
        break
x = t[i:]
for j in range(k - 1):
    t = t + x
print(t)
