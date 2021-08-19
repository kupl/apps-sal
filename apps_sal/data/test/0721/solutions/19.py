def M():
    return map(int, input().split())


def L():
    return list(map(int, input().split()))


def I():
    return int(input())


(n, d) = M()
(a, k) = (sorted(L()), I())
print(sum(a) + (n - k) * d if n < k else sum(a[:k]))
