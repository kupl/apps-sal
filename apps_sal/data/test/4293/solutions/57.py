(P, Q, R) = map(int, input().split())
max_d = max(P, max(Q, R))
total = P + Q + R - max_d
print(total)
