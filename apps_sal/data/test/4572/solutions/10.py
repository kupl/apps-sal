S = str(input())
al = [chr(ord('a') + i) for i in range(26)]
data = []
for x in S:
    if not x in data:
        data.append(x)
ans = list(set(al) ^ set(data))
ans.sort()
if len(ans) == 0:
    print('None')
else:
    print(ans[0])
