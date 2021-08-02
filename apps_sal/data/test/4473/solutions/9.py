import math
for _ in range(int(input())):
    a, b, k = list(map(int, input().split()))
    ans = a * math.ceil(k / 2) - b * (k // 2)
    print(ans)
