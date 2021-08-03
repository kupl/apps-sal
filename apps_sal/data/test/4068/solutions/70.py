N, M = [int(i) for i in input().split()]
AS = {int(input()) for _ in range(M)}

t = [1, 1 if 1 not in AS else 0]
for i in range(2, N + 1):
    #  print(t)
    if i in AS:
        t.append(0)
        continue
    t.append(t[i - 2] + t[i - 1])

# print(t)
print((t[N] % 1000000007))
