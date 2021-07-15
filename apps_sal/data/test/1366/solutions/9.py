n = int(input())
a, b, p = [0] * n, [0] * n, {}
for i in range(n):
    a[i], b[i] = input().split()
    p[b[i]] = (a[i] != b[i] or b[i] in p)
print(sum(not a[i] in p or (p[a[i]] == 0 and a[i] == b[i]) for i in range(n)))
