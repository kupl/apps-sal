n = int(input())

lst = []
for i in range(1, n + 1):
    s, p = input().split()
    lst.append([i, s, -int(p)])
lst.sort(key=lambda x: (x[1], x[2]))
for i in lst:
    print(i[0])
