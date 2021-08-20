import math
N = int(input())
A_list = list(map(int, input().split()))
ans = A_list[0]
for i in range(N - 1):
    ans = math.gcd(A_list[i + 1], ans)
print(ans)
