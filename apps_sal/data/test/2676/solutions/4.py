n = int(input())
l = []
for i in range(n):
    l.append(input())
m = int(input())
b = input()
d = set()
for i in range(n):
    if(l[i] in b):
        d.add(l[i])
print(len(list(d)))
