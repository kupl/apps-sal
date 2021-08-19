n = [int(input()) for i in range(4)]
print(sum((0 <= (n[3] - 500 * a - 100 * b) // 50 <= n[2] and (n[3] - 500 * a - 100 * b) % 50 == 0 for a in range(n[0] + 1) for b in range(n[1] + 1))))
