n = int(input())
d = {}
for i in range(n):
    s = input()
    d[s] = d.get(s, 0) + 1
print(len(d))
