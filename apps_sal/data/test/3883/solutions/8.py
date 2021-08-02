def run1(x, y):
    if x < y:
        return -1;
    cst = (x - y) * 0.5;
    l = 1; r = 1000000001;
    ans = - 1.0;
    while(l <= r):
        m = (l + r) >> 1;
        now = cst / m;
        if now >= y:
            ans = now;
            l = m + 1;
        else:
            r = m - 1;
    return ans;


def run2(x, y):
    cst = (x + y) * 0.5;
    l = 1; r = 1000000001;
    ans = - 1.0;
    while(l <= r):
        m = (l + r) >> 1;
        now = cst / m;
        if(now >= y):
            ans = now;
            l = m + 1;
        else:
            r = m - 1;
    return ans;


x, y = list(map(int, input().split()));
p = run1(x, y);
q = run2(x, y);

ans = - 1.0;

if(ans < 0 or (p > 0 and p < ans)):
    ans = p;
if(ans < 0 or (q > 0 and q < ans)):
    ans = q;
print(ans)
