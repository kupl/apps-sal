n = int(input())
cl = list(map(int, input().split()))
s = input()
dic = {}
for x in range(n):
    dic.update({cl[x]: x + 1})
cl = sorted(cl)
pl = []
res = ''
pos1 = 0
for c in s:
    if c == '0':
        pl.append(cl[pos1])
        res += str(dic[cl[pos1]]) + ' '
        pos1 += 1
    if c == '1':
        mx = pl[-1]
        res += str(dic[mx]) + ' '
        pl.pop(-1)
print(res)
