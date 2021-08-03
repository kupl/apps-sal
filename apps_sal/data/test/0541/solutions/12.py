n, m = list(map(int, input().split()))
ba = []
for i in range(m):
    a, b = [int(x) - 1 for x in input().split()]
    ba.append((b, a))
ba.sort()
count = 0
prev_b = -1
for b, a in ba:
    if a < prev_b:
        continue
    prev_b = b
    count += 1
print(count)
