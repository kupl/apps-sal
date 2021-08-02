n, k = list(map(int, input().split()))
a = [int(x) % k for x in input().split()]
f = {}
an = 0
for i in a:
    if -i in f and f[-i] > 0:
        an += 2
        f[-i] -= 1
    elif k - i in f and f[k - i] > 0:
        an += 2
        f[k - i] -= 1
    else:
        if i not in f: f[i] = 0
        f[i] += 1
print(an)
