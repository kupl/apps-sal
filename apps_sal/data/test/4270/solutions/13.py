n = int(input())
v = list(map(int, input().split()))
v = sorted(v)
count = v[0]
for i in range(1, n):
    count = (count + v[i]) / 2
print(count)
