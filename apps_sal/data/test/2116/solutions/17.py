n, m, k = map(int, input().split())
s = list(map(int, input().split()))
d = 0
for i in range(n):
    for a in list(map(int, input().split())):
        for j in range(k):
            if s[j] == a:
                del(s[j])
                s = [a] + s
                d += j + 1
print(d)
