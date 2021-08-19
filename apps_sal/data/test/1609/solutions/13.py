from collections import Counter
n = int(input())
A = list(map(int, input().split()))


def change():
    set_list = set(A)
    for i in range(1, n + 1):
        if i not in set_list:
            yield i


C = Counter(A)
ch = change()
for i in range(n):
    if C[A[i]] > 1:
        C[A[i]] -= 1
        A[i] = next(ch)
    elif A[i] > n:
        A[i] = next(ch)
for i in A:
    print(i, end=' ')
