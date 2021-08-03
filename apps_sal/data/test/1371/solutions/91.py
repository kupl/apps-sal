S = int(input())
anslist = []
anslist.extend([1, 0, 0])
for i in range(3, S + 1):
    ansi = anslist[i - 3] + anslist[i - 1]
    anslist.append(ansi)
ans = anslist[S] % (10**9 + 7)
print(ans)
