t = [[], [], []]
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    t[a[i] - 1].append(i + 1)
m = 1e9
for i in t:
    m = min(len(i), m)
print(m)
for i in range(m):
    print(t[0][i], t[1][i], t[2][i])
