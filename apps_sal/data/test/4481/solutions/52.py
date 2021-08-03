n = int(input())
dd = {}
for i in range(n):
    s = input()
    if s in dd.keys():
        dd[s] += 1
    else:
        dd[s] = 1
ma = max(dd.values())
lst = []
for k, v in dd.items():
    if v == ma:
        lst.append(k)
for l in sorted(lst):
    print(l)
