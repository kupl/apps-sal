n = int(input())
d = []
for i in range(n):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        d.append(i)
result = 'No'
if len(d) <= 2:
    print(result)
else:
    for h in range(len(d) - 2):
        if d[h] == d[h + 1] - 1 == d[h + 2] - 2:
            result = 'Yes'
            break
    print(result)
