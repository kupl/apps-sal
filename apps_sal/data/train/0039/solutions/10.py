t = int(input())
for _ in range(t):
    a, b, p = map(int, input().split())
    s = list(input())
    n = len(s)
    flg = 0
    ans = n
    y = "C"
    k = 0
    while s:
        x = s.pop()
        if not flg:
            flg = 1
            continue
        if x == y:
            ans -= 1
            continue
        else:
            if x == "A":
                if p < a:
                    print(ans)
                    k = 1
                    break
                else:
                    p -= a
            if x == "B":
                if p < b:
                    print(ans)
                    k = 1
                    break
                else:
                    p -= b
        y = x
        ans -= 1
    if s == [] and k == 0:
        print(1)
