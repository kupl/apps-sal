n, m = map(int, input().split())
a = [0] * m
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == '*':
            if a[j] == 0:
                a[j] = n - i

spusk = 0
pod = 0
for i in range(m - 1):
    p = a[i + 1] - a[i]
    if p > 0:
        if p > pod:
            pod = p
    else:
        p *= (-1)
        if spusk < p:
            spusk = p

print(pod, spusk)
