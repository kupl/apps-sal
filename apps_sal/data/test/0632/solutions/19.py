t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    div = -1
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            div = i
            break
    if div == -1:
        div = n
    n += div
    k -= 1
    print(n + k * 2)
