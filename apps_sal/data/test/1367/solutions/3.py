n = int(input())
a = set(input().split())
b = set()
for i in range(1, n + 1):
    b.add(str(i))
for i in b.difference(a):
    print(i)
