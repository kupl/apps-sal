n = int(input())
v = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))
res = 0
for i in range(n):
    eco = v[i] - c[i]
    if eco > 0:
        res += eco
print(res)
