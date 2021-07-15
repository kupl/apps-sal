n =  int(input())
s = input()
t = input()
a, b = [], []
for i in range(n):
    if(s[i] != t[i]):
        if(s[i] == 'a'):
            a.append(i+1)
        else:
            b.append(i+1)
m = len(a) + len(b)
if(m&1):
    print(-1)
else:
    ans = m//2
    if(len(a)&1):
        ans += 1
    print(ans)
    if(len(a)&1):
        print(a[-1], a[-1])
        print(a[-1], b[-1])
    for i in range(0, len(a)-1, 2):
        # print(i)
        print(a[i], a[i+1])
    for i in range(0, len(b)-1, 2):
        print(b[i], b[i+1])

