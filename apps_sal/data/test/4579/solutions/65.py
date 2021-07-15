n = int(input())
d = {}
for _ in range(n):
    s = input()
    if not s in d.keys():
        d[s] = 1
print(len(d))
