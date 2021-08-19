n = int(input())
res = []
a = [[0] * n] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(n):
    # print(a[i].count(2))
    if a[i].count(1) > 0:
        continue
    elif a[i].count(3) == 0:
        res.append(i + 1)
'''for j in range(n):
    if a[i].count(2)>0:
        continue
    elif a[i].count(3)==0:
        res.append(i+1)'''
if len(res) == 0:
    print(0)
    quit()
print(len(res))
res.sort()
print(' '.join(map(str, res)))
