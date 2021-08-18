import math
N = int(input())
ans = 0
if N == 0 or N % 2 == 1:
    ans = 0
else:
    digN = round(math.log(N, 5))

    i = 1
    while i <= digN:
        ans += (N // (5 ** i * 2))
        i += 1

print(ans)
