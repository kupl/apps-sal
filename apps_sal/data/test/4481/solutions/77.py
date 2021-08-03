n = int(input())
a = {}
for i in range(n):
    s = input()
    if s not in a:
        a.update({s: 0})
    else:
        temp = a[s] + 1
        a.update({s: temp})
max_val = max(list(a.values()))
b = []
for key in a:
    if a[key] == max_val:
        b.append(key)
b.sort()
print(*b, sep='\n')
