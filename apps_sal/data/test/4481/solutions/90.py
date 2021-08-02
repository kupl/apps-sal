n = int(input())

l = {}
a = 0

for i in range(n):
    s = input()
    if s in l:
        l[s] += 1
    else:
        l[s] = 1
    if a < l[s]:
        a = l[s]
ans = []

for i in list(l.keys()):
    if l[i] == a:
        ans.append(i)

ans.sort()

for j in ans:
    print(j)
