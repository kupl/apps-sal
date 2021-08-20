n = int(input())
a = [list(map(int, input().split())), list(map(int, input().split()))]
m = [a[0][-1], a[1][-1]]
for i in list(range(n - 1))[::-1]:
    (m[0], m[1]) = (max(m[0], m[1] + a[0][i]), max(m[1], m[0] + a[1][i]))
print(max(m[0], m[1]))
