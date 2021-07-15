n, k = map(int, input().split())
k = int(k)
s = input()
s = "Y" + s + "Y"
res = "NO"
cnt = 0
can = True
for ch in s:
    if(ch == 'N'):
        cnt += 1
        if(cnt > k):
            can = False
    else:
        cnt = 0

for i in range(1,n+1):
    if(i + k - 2 < n):
        subs = s[i:i+k]
        # print(subs)
        flag = True
        for ch in subs:
            if(not ch in "N?"):
                flag = False
        if((s[i-1] in "Y?" and s[i+k] in "Y?") and flag):
            res = "YES"
            # print(s[i-1], subs, s[i+k])
if can:
    print(res)
else:
    print("NO")
