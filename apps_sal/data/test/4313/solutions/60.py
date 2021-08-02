n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
cost = []
for i in range(n):
    if v[i] - c[i] > 0:
        cost.append(v[i] - c[i])
print(sum(cost))
