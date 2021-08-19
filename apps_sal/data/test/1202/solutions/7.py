n = int(input())
(a, b) = zip(*(map(int, input().split()) for _ in range(n)))
i = j = 0
while i < n and j < n and (i + j < n):
    if a[i] < b[j]:
        i += 1
    else:
        j += 1


def p(x):
    return ('1' * max(n // 2, x)).ljust(n, '0')


print(p(i))
print(p(j))
