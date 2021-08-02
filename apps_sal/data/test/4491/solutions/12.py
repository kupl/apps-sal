n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
tmp = []
cnd = 0
for i in range(n):
    cnd = sum(a[:i + 1]) + sum(b[i:])
    tmp.append(cnd)
    cnd = 0
print(max(tmp))
