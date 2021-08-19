(n, k) = list(map(int, input().split()))
t = input()
a = 0
for i in range(1, n):
    if t[i:] == t[:-i]:
        a = i
        break
if not a:
    print(t * k)
else:
    print(t + t[n - a:] * (k - 1))
