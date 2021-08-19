s = input()
t = input()
revS = s[::-1]
n = len(s)
cur = 1
start = -1
end = -1
revFlag = 0
errFlag = 0
i = 0
res = []
while i < len(t):
    if s.find(t[i:i + cur]) != -1 and i + cur <= len(t) and (s.find(t[i:i + cur]) + cur <= n):
        start = s.find(t[i:i + cur]) + 1
        end = start + cur - 1
        cur += 1
    elif revS.find(t[i:i + cur]) != -1 and i + cur <= len(t) and (revS.find(t[i:i + cur]) + cur <= n):
        start = n - revS.find(t[i:i + cur])
        end = start - cur + 1
        cur += 1
    else:
        if (start == -1 and end == -1) and (s.find(t[i:i + cur]) == -1 and revS.find(t[i:i + cur]) == -1):
            errFlag = 1
            break
        i += cur - 1
        cur = 1
        res.append(str(start) + ' ' + str(end))
        start = -1
        end = -1
if errFlag != 1:
    print(len(res))
    for p in res:
        print(p)
else:
    print(-1)
