n, t = int(input()) - 1, [0] * 101
a, b = map(int, input().split())
for i in range(n) :
    l, r = map(int, input().split())
    t[l] += 1
    t[r] -= 1
for i in range(b - 1): t[i + 1] += t[i]
print(t[a: b].count(0))
