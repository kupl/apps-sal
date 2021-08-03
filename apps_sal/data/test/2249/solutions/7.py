n = int(input())
a = list(map(int, input().split()))

right = list()
s = set()

for el in a[::-1]:
    s.add(el)
    right.append(len(s))

right = right[::-1]

s = set()
ans = 0

for i, el in enumerate(a[:-1]):
    if el not in s:
        ans += right[i + 1]

    s.add(el)

print(ans)
