n = int(input())
a = list(map(int, input().split()))
md = a[0] % 2
found = False
for x in a:
    if x % 2 != md:
        found = True
if found:
    a.sort()
for x in a:
    print(str(x) + ' ', end='')
