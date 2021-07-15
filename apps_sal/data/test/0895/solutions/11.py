n, t = input(), [0] * 1002
for i in map(int, input().split()): t[i] += 1
T = int(input()) + 1
for i in range(1000): t[i + 1] += t[i]
print(max(t[i + T] - t[i] for i in range(-1, 1001 - T)))
