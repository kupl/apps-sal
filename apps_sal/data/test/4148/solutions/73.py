N = int(input())
S = input()
c = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

ans = ''
for i in range(len(S)):
    ans += c[(c.index(S[i]) + N) % 26]

print(ans)
return

