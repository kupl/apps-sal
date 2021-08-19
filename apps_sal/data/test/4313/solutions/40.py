n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
m = 0
for i in range(len(v)):
    if v[i] > c[i]:
        m += v[i] - c[i]
print(m)
