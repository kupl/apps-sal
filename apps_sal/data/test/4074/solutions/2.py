
import math

T = int(input())

for _ in range(T):
    n, k = list(map(int, input().split()))

    divs = set()
    for d in range(1, int(math.sqrt(n)) + 2):
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)

    ans = 10**10
    for d in divs:
        if d > k:
            continue
        else:
            ans = min(ans, n // d)

    print(ans)

