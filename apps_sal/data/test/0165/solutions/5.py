(B, L, S) = (int(x) for x in input().split())
K = max(B, L, S)
cost = 0
for meal in [B, L, S]:
    if meal != K:
        cost += K - 1 - meal
print(cost)
