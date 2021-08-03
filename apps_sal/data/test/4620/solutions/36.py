n = int(input())
l = []
for _ in range(n - 1):
    c, s, f = map(int, input().split())
    for i, t in enumerate(l):
        if t > s:
            t = -(-t // f) * f
        else:
            t = s
        l[i] = t + c
    l += [s + c]
for i in l + [0]:
    print(i)
