(P, Q, R) = map(int, input().split())
sums = [P + Q, R + Q, Q + R, P + R, R + P, Q + P]
print(min(sums))
