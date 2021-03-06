n = int(input())
ai = [int(x) for x in input().split()]
mcDigit = 0
for i in range(9):
    if ai[i] <= ai[mcDigit]:
        mcDigit = i
di = [x - mcDigit for x in ai]
resLen = n // ai[mcDigit]
res = [mcDigit] * resLen
remain = n - resLen * ai[mcDigit]
for i in range(resLen):
    if remain <= 0:
        break
    d = 8
    while d > mcDigit:
        if remain >= ai[d] - ai[mcDigit]:
            res[i] = d
            remain -= ai[d] - ai[mcDigit]
            break
        d -= 1
    if d == mcDigit:
        break
out = ''
for i in res:
    out = out + str(i + 1)
if resLen == 0:
    print('-1')
else:
    print(out)
