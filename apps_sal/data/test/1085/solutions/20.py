import math
N = int(input())
ans = 0
for i in range(1, int(math.sqrt(N - 1)) + 1):
    if (N - 1) % i == 0:
        ans += 2
        i += 1
    else:
        i += 1
ans -= 1
if int(math.sqrt(N - 1)) == math.sqrt(N - 1):
    ans -= 1
for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
        temp = N
        while temp % i == 0:
            temp = temp / i
        if temp % i == 1:
            ans += 1
            i += 1
        else:
            i += 1
ans += 1
print(ans)
