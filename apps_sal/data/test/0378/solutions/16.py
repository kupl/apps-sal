K, R = (int(x) for x in input().split())
a = K % 10
cost = 0
val = 10
for i in range(1, 11):
    cost += a
    if cost % 10 in [0, R]:
        val = i
        break

print(val)
