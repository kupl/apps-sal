n = int(input());
s = map(int, input().split());
i = 0;
k = 0;
t = 0;
x = 0;
c = 0;
ans = 1;
for i in list(s):
    p = int(i);
    if (c == 0):
        if (k == 0):
            t = p;
        if (t == p):
            k += 1
        else:
            t = p;
            x = 0;
            c = 1;
    if (t == p):
        x += 1
    else:
        t = p;
        if (x != k):
            ans = 0;
        x = 1;
if (x != k):
    ans = 0;
if (ans == 1):
    print('YES')
else:
    print('NO')
