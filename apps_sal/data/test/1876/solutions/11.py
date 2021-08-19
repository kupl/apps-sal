def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) % (10 ** 9 + 7)


(n, k) = [int(i) for i in input().split()]
s = [[] for i in range(n)]
for i in range(n - 1):
    (a, b, c) = [int(i) for i in input().split()]
    if c == 0:
        s[a - 1].append(b - 1)
        s[b - 1].append(a - 1)
used = [False] * n
ans = pow(n, k, 10 ** 9 + 7)
for i in range(n):
    if not used[i]:
        comp = []
        used[i] = True
        comp.append(i)
        c = 0
        while c < len(comp):
            for h in s[comp[c]]:
                if not used[h]:
                    used[h] = True
                    comp.append(h)
            c += 1
        ans = (ans - pow(len(comp), k, 10 ** 9 + 7)) % (10 ** 9 + 7)
print(ans)
