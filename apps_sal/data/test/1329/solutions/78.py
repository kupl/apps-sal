def num_div(n):
    p = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            p.append(i)
            n //= i
    if n > 1:
        p.append(n)
    return p


n = int(input())
x = [0] * (n + 1)
for i in range(1, n + 1):
    for j in num_div(i):
        x[j] += 1
ex2 = len([i for i in x if i > 1])
ex4 = len([i for i in x if i > 3])
ex14 = len([i for i in x if i > 13])
ex24 = len([i for i in x if i > 23])
ex74 = len([i for i in x if i > 73])
print(ex4 * (ex4 - 1) // 2 * (ex2 - 2) + ex24 * (ex2 - 1) + ex14 * (ex4 - 1) + ex74)
