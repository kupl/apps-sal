(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
powers = set()
for i in range(0, 100):
    p = k ** i
    if abs(p) > 10 ** 9 * 10 ** 5:
        break
    else:
        powers.add(p)
s = [0]
for e in a:
    s.append(s[-1] + e)
result = 0
freq = {}
for i in range(0, n + 1):
    for p in powers:
        sx = s[i] - p
        if sx in freq:
            result += freq[sx]
    freq.setdefault(s[i], 0)
    freq[s[i]] += 1
print(result)
