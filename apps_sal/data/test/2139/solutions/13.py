s = input()
n = len(s)

idx = [-1]
curIdx = s.find('bear', 0)
cnt = 1
while curIdx > -1:
    idx.append(curIdx)
    cnt = cnt + 1
    curIdx = s.find('bear', curIdx + 1)
    
ret = 0
for i in range(cnt - 1):
    ret = ret + (idx[i + 1] - idx[i]) * (n - idx[i + 1] - 3)

print(ret)

