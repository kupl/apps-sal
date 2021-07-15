n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1

rec = []
for i in range(n):
    s = set()
    k = i
    while k not in s:
        s.add(k)
        k = a[k]

    rec.append(k + 1)

print(" ".join(map(str, rec)))
