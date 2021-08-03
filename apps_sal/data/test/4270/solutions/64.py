n = int(input())
v = list(map(int, input().split()))
v = sorted(v)
a = (v[0] + v[1]) / 2
for i in range(2, n):
    a = (a + v[i]) / 2
print(a)
