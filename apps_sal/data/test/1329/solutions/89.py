n = int(input())

if n < 10:
    print((0))
    return

prime = [2, 3]
for i in range(5, n+1, 2):
    for p in prime:
        if i % p == 0:
            break
    else:
        prime.append(i)

# factrization
num = []
for p in prime:
    cnt = 1
    now = p
    while now <= n:
        cnt += n // now
        now *= p
    num.append(cnt)

more3 = [i for i in num if i >= 3]
more5 = [i for i in more3 if i >= 5]
more15 = [i for i in more5 if i >= 15]
more25 = [i for i in more15 if i >= 25]
more75 = [i for i in more25 if i >= 75]

more3 = len(more3); more5 = len(more5); more15 = len(more15); more25 = len(more25); more75 = len(more75)

print((more25 * (more3 - 1) + more15 * (more5 - 1) + more5 * (more5 - 1) * (more3 - 2) // 2 + more75))

