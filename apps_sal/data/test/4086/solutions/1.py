n = int(input())

lst = [int(x) for x in input().split()]

a = []
for x in range(n - 1, -1, -1):
    if not lst[x] in a:
        a.append(lst[x])

a.reverse()
print(len(a))
print(*a)

