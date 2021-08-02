n = int(input())
lst = []
for i in range(n):
    d = int(input())
    lst.append(d)
res = sorted(list(set(lst)))
print(len(res))
