l, r = map(int, input().split());
def f(a):
    ans = 1;
    for q in range(2, a + 1):
        ans *= q;
    return ans;
def much(l):
    a = 1;
    cnt = -1;
    while a <= l:
        a = a * 3;
        cnt = cnt + 1;
    k3 = cnt;
    a1 = 1;
    cnt = -1;
    while a1 <= l:
        a1 = a1 * 2;
        cnt = cnt + 1;
    k2 = cnt; # (k3 + 2) 
    ans = (k3 + 1) * (k3 + 2) // 2;
    #print(k2);
    for q in range(k3 + 1, k2 + 1):
        x = 2 ** q;
        while 1:
            ans += 1;
            x = x * 3 // 2;
            if x > l:
                break;
    return ans;
k = much(r) - much(l - 1);
print(k);
