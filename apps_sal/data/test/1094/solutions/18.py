n = int(input())
name = {}
for i in range(n):
    s = input()
    name[s] = i
a = list(name)
a.sort(key=lambda x: -name[x])
for i in range(len(a)):
    print(a[i])
