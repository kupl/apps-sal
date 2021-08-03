import math
N = int(input())
lst = list(map(int, input().split()))
X = math.floor(sum(lst) / N + 0.5)
ans = 0
for i in lst:
    ans = ans + (X - i)**2

print(ans)
