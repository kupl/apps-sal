def solve(A, n, m):
    uniq = set(A)
    odd = list([x for x in uniq if x % 2])
    even = list([x for x in uniq if x % 2 == 0])
    if len(odd) > n // 2:
        odd.sort()
        odd = odd[-n // 2:]
    if len(even) > n // 2:
        even.sort()
        even = even[-n // 2:]

    odd_needed = n // 2 - len(odd)
    changes = n - len(odd) - len(even)
    k = 1 if odd_needed else 2

    D = {x: True for x in odd + even}
    A1 = A[:]
    for i, a in enumerate(A):
        if a in D and D[a]:
            D[a] = False
        else:
            while k in D:
                k += 2
            if k > m:
                return None
            A1[i] = k
            k += 2
            if odd_needed == 1:
                k = 2
            if odd_needed >= 1:
                odd_needed -= 1

    return A1, changes


n, m = list(map(int, input().split()))
A = [int(x) for x in input().split()]
p = solve(A, n, m)
if p is None:
    print(-1)
else:
    print(p[1])
    print(' '.join(map(str, p[0])))
