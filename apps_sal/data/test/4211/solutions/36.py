n = int(input())
alist = list(map(int, input().split()))
alist.insert(0, 10000000.0)
alist.append(10000000.0)
core = 0
for i in range(n):
    core += min(alist[i], alist[i + 1])
print(core)
