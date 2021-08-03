import string
n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
sl = [list(input()) for i in range(n)]

alpha = list(string.ascii_lowercase)

dic = {si: sl[0].count(si) for si in alpha}

for s in sl:
    for ch in alpha:
        dic[ch] = min(dic[ch], s.count(ch))
ans = ''
for ch in alpha:
    for i in range(dic[ch]):
        ans += ch
print(ans)
