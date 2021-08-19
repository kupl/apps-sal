def g(a, k):
    if a == 0:
        return k == 0
    s = set()
    while a > 0:
        if a % 10 <= k:
            s.add(a % 10)
        a //= 10
    return len(s) == k + 1


(n, k) = (int(x) for x in input().split())
print(sum((g(int(input()), k) for i in range(n))))
