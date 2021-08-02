import math
from scipy.special import comb
N, D = map(int, input().split())
List = []

for i in range(N):
    x = list(map(int, input().split()))
    List.append(x)

ans = 0
for i in range(N - 1):
    y = List[i]

    for j in range(i + 1, N):
        z = List[j]
        sum = 0
        for j in range(D):
            sum += abs(y[j] - z[j])**2
            s = math.sqrt(sum)

        if s.is_integer():
            ans += 1

print(ans)
