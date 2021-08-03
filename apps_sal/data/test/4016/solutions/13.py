n, k = list(map(int, input().split()))
s = input()

res = n
for i in range(1, n):
    if s.startswith(s[i:]):
        res = i
        break
overlap = n - res

print(s + (k - 1) * s[overlap:])
