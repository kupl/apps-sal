import math

S, P = list(map(int, input().split()))
i_max = int(math.sqrt(P)) + 1

ans = "No"
for i in range(1, i_max):
    if P % i == 0:
        q = P // i
        if (i + q) == S:
            ans = "Yes"
            break

print(ans)
