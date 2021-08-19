from itertools import accumulate


def eratosthenes(n):
    table = [0] * (n + 1)
    prime_list = []
    for i in range(2, n + 1):
        if table[i] == 0:
            prime_list.append(i)
            for j in range(i + i, n + 1, i):
                table[j] = 1
    return prime_list


n = 100000
prime_list = set(eratosthenes(n))
a = []
for i in range(n):
    if i in prime_list and (i + 1) // 2 in prime_list:
        a.append(1)
    else:
        a.append(0)
a = list(accumulate(a))
q = int(input())
for _ in range(q):
    (l, r) = map(int, input().split())
    print(a[r] - a[l - 1])
