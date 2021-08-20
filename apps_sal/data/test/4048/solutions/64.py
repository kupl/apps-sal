import math
N = int(input())
ans = 10 ** 12
for i in range(1, math.ceil(math.sqrt(N)) + 2):
    if N % i == 0:
        tem = N // i + N // (N // i) - 2
        if tem <= ans:
            ans = tem
print(ans)
