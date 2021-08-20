N = int(input())
P = []
for i in range(N):
    P.append(int(input()))
total_price = max(P) // 2 + (sum(P) - max(P))
print(total_price)
