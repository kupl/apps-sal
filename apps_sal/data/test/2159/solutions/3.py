n = int(input())
t = [int(q) - 1 for q in input().split()]
k = [0] * n
for i in range(n):
    s = [0] * n
    b = 0
    for a in t[i:]:
        s[a] += 1
        if s[a] > s[b] or (a < b and s[a] == s[b]):
            b = a
        k[b] += 1
print(*k)
