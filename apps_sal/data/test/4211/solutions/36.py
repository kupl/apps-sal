n = int(input())
alist = list(map(int, input().split()))
alist.insert(0, 1e7)
alist.append(1e7)
core = 0
for i in range(n):
    core += min(alist[i], alist[i + 1])
print(core)
