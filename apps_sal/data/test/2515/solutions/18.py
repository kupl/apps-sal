def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return 0
    return 1


sl = [0, 0]
for j in range(2, 10 ** 5 + 1):
    if j % 2 == 0:
        sl.append(sl[j - 1])
    elif is_prime(j) == 1 and is_prime((j + 1) // 2) == 1:
        sl.append(sl[j - 1] + 1)
    else:
        sl.append(sl[j - 1])

q = int(input())
for _ in range(q):
    l, r = list(map(int, input().split()))
    print((sl[r] - sl[l-1]))

