from collections import Counter
n = int(input())
cnt = Counter(input())
odd = []
even = []
for s, c in cnt.items():
    if c % 2 == 1:
        odd.append([s, c])
    else:
        even.append([s, c])
k = max(1, len(odd))
for i in range(k, n + 1):
    h = n // i
    if i * h == n and (not odd and h % 2 == 0 or odd and h % 2 == 1):
        k = i
        break
h = n // k
res = []
while len(res) < k:
    if odd:
        s, c = odd.pop()
        res.append(s)
        c -= 1
        if c:
            even.append([s, c])
    elif h % 2:
        res.append(even[0][0])
        res.append(even[0][0])
        even[0][1] -= 2
        if not even[0][1]:
            even.pop(0)
    else:
        res.append('')
for i in range(k):
    s = res[i]
    while len(s) < h:
        t = (h - len(s)) // 2
        a, c = even[0]
        if c <= 2 * t:
            c //= 2
            s = a * c + s + a * c
            even.pop(0)
        else:
            s = a * t + s + a * t
            even[0][1] -= 2 * t
    res[i] = s

print(len(res))
print(' '.join(res))
