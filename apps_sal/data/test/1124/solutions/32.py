import math
N = int(input())
A_lst = list(map(int, input().split()))
A_lst.sort()
ans = A_lst[0]
for i in range(1, N):
    ans = math.gcd(ans, A_lst[i])
print(ans)
