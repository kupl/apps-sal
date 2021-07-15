n = int(input())
li = set()

for i in range(n):
    x = int(input())
    if x in li:
        li.remove(x)
    else:
        li.add(x)
print((len(li)))

