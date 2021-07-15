n = int(input())
ans = list()
s = set()
for i,x in enumerate(map(int, input().split())):
    if not s:
        idx = i+1
    elif x in s:
        ans.append((idx, i+1))
        s = set()
        continue
    s.add(x)
if len(ans):
    ans[-1] = (ans[-1][0], n)
    print(len(ans))
    print('\n'.join('%d %d' % p for p in ans))
else:
    print(-1)
