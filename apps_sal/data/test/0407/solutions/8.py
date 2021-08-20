n = int(input())
lin = 'abcdefghij'
wei = [[0, False] for i in range(10)]
weig = [i for i in range(10)]
inp = []
for i in range(n):
    inp.append(input())
inp.sort(key=len)
n = len(inp[-1])
for i in inp:
    m = len(i)
    wei[lin.index(i[0])][1] = True
    for j in range(m):
        wei[lin.index(i[j])][0] += 10 ** (m - j - 1)
wei.sort(reverse=True)
ans = 0
for i in wei:
    if i[1] and weig[0] == 0:
        ans += i[0] * weig[1]
        weig.remove(weig[1])
    else:
        ans += i[0] * weig[0]
        weig.remove(weig[0])
print(ans)
