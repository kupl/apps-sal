n = int(input())
div = []
div2 = []
ans = 0
for i in range(1, 10 ** 6 + 1):
    if n % i == 0:
        div += [i, n // i]
    if (n - 1) % i == 0:
        div2 += [i, (n - 1) // i]
div = set(div)
div2 = set(div2)
a = [1]
for i in div:
    if i > 1:
        t = n
        while t:
            if t % i == 0:
                t = t // i
            else:
                if t % i == 1:
                    ans += 1
                    a += [i]
                break
for i in div2:
    a += [i]
a = set(a)
print(len(a) - 1)
