(n, q, l) = list(map(int, input().split()))
a = [0] + list(map(int, input().split())) + [0]
t = 0
s = [False] * (n + 2)
for i in range(1, n + 1):
    if a[i] > l:
        if s[i - 1] == False:
            t += 1
        s[i] = True
for i in range(q):
    k = input()
    if k[0] == '0':
        print(t)
    else:
        (k, p, d) = list(map(int, k.split()))
        a[p] += d
        if a[p] > l and s[p] == False:
            if s[p - 1] and s[p + 1]:
                t -= 1
            elif s[p - 1] == False and s[p + 1] == False:
                t += 1
            else:
                pass
            s[p] = True
