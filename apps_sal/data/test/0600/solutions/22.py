a = int(input());
b = int(input());
r = abs(a - b);
ca = 1;
cb = 1;
ans = 0;
while r > 0:
    r = r - 1;
    ans = ans + ca;
    ca = ca + 1;
    if r <= 0:
        break;
    r = r - 1;
    ans = ans + cb;
    cb = cb + 1;
print(ans);
