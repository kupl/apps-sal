def cal(n):
    m = n
    ret = 0
    while n != 0:
        ret += n % 10
        n //= 10
    return m/ret

# n以上で s(n) が最小となる整数値
def f(n):
    cand = []
    s = str(n)
    for i in range(len(s)-1,-1,-1):
        if s[i] == "9":
            continue
        for j in range(int(s[i]), 10):
            t = int(s[:i] + str(j) + s[i+1:])
            cand += [ t ]
        s = s[:i] + "9" + s[i+1:]

    ret = n
    for x in cand:
        if cal(x) < cal(ret):
            ret = x
    return ret 


k = int(input())
ans = 1

for _ in range(k):
    print(ans)
    ans = f(ans+1)

