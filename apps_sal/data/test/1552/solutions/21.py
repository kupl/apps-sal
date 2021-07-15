n = int(input())
t = list(map(int, input().split()))
a = [[] for i in range(3)]
for i, m in enumerate(t):
    a[m-1].append(i+1)
w = min(list(map(len, a)))
print(w)
for i in range(w):
    print(a[0][i], a[1][i], a[2][i])

