(k, a, b) = list(map(int, input().split()))
a1 = a // k
r_a1 = a % k
b1 = b // k
r_b1 = b % k
if a1 + b1 == 0 or (min(a, b) < k and max(a, b) % k != 0):
    print(-1)
else:
    print(a1 + b1)
