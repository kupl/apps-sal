n = int(input())
a = set()
for i in range(n):
    x = int(input())
    if x in a:
        a.discard(x)
    else:
        a.add(x)
print(len(a))
