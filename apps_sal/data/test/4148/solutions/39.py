n = int(input())
s = input()
al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ""

for i in s:
    ind = al.index(i) + n
    ans += al[ind % 26]

print(ans)
