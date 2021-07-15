n = int(input())
a = list(map(int, input().split()))

a.sort()

t = a[0]
for x in a:
    if x % a[0] != 0:
        t = -1

print(t)
