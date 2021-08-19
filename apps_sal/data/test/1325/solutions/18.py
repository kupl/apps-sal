(n, p) = map(int, input().split())
p -= 1
s = input()
arr = [(lambda x, y: min(abs(x - y), 26 - abs(y - x)))(ord(s[i]), ord(s[n - i - 1])) for i in range(n // 2)]
p = min(p, n - p - 1)
(f, l) = (0, len(arr) - 1)
for a in arr:
    if a != 0:
        break
    else:
        f += 1
for a in reversed(arr):
    if a != 0:
        break
    else:
        l -= 1
print(sum(arr) + l - f + min(abs(p - l), abs(p - f)) if sum(arr) > 0 else 0)
