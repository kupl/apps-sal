n = int(input())
a = list(map(int, input().split()))

d = [0 for _ in range(4)]

for val in a:
    if val == 1:
        d[0] += 1
        d[2] = max(d[2] + 1, d[1] + 1)
    else:
        d[1] = max(d[1] + 1, d[0] + 1)
        d[3] = max(d[3] + 1, d[2] + 1)
print(max(d))
