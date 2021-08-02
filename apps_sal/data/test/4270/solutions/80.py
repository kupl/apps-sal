n = int(input())
lst = list(map(int, input().split()))
lst.sort()
for i in range(n - 1):
    x = (lst[0] + lst[1]) / 2
    lst.pop(0)
    lst.pop(0)
    lst.append(x)
    lst.sort()
print((lst[0]))
