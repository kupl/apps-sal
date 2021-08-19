from itertools import combinations
N = int(input())
st = input()
n = len(st)
mx = ''
ans = False
a = [st[x:y] for (x, y) in combinations(range(len(st) + 1), r=2)]
for i in a:
    for j in range(len(i) // 2):
        if i[j] == i[-1 - j]:
            ans = True
        else:
            ans = False
            break
    if ans == True:
        if len(mx) < len(i):
            mx = i
print(len(mx))
print(mx)
