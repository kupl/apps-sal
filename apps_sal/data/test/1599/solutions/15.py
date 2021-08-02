s = input()
n = int(input())

l, r = [0 for i in range(n)], [0 for i in range(n)]
for i in range(n):
    l[i], r[i] = list(map(int, input().split()))

d = [0] * len(s)
for i in range(len(s) - 1):
    d[i + 1] = d[i]
    if(s[i] == s[i + 1]):
        d[i + 1] = d[i] + 1

for i in range(n):
    print(d[r[i] - 1] - d[l[i] - 1])
