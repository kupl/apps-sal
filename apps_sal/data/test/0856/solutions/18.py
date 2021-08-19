t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    first = list(map(int, input().split()))
    k -= 1
    m = max(first)
    for i in range(n):
        first[i] = m - first[i]
    second = first.copy()
    m = max(second)
    for i in range(n):
        second[i] = m - second[i]
    if k % 2 == 0:
        print(*first)
    else:
        print(*second)
