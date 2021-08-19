N = int(input())
s = []
for i in range(N):
    s.append(int(input()))
s.sort()
ans = sum(s)
if ans % 10 == 0:
    fil = list(filter(lambda x: x % 10 != 0, s))
    if len(fil) == 0:
        print(0)
    else:
        print(ans - fil[0])
else:
    print(ans)
