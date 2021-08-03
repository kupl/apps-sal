
s = input().split()
n = int(s[0])
m = int(s[1])
mp = list(map(int, input().split()))
neg = 0
pos = 0
for k in mp:
    if k == -1:
        neg += 1
    else:
        pos += 1

mine = min(neg, pos)
ans = ""
while m > 0:
    m -= 1
    st = input().split()
    l = int(st[0])
    r = int(st[1])
    dif = r - l + 1
    if dif % 2 == 0 and dif // 2 <= mine:
        ans += "1\n"
    else:
        ans += "0\n"
print(ans)
