n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
a = []
for i in range(n):
    if v[i] > c[i]:
        a.append(v[i] - c[i])
print(sum(a))
