a, b, t = int(input()), list(map(int, input().split())), 0
c = [0] * a
for i in range(a):
    c[b[i] - 1] = i
for i in range(a - 1):
    t += abs(c[i] - c[i + 1])
print(t)
