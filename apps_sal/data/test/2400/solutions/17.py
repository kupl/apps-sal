t = int(input())
for _ in range(t):
    n = int(input())
    pis = list(map(int, input().split()))
    m = int(input())
    qis = list(map(int, input().split()))

    even = sum([1 if pi % 2 == 0 else 0 for pi in pis])
    odd = sum([1 if pi % 2 == 1 else 0 for pi in pis])
    ans = 0
    for qi in qis:
        if qi % 2 == 0:
            ans += even
        else:
            ans += odd
    print(ans)
