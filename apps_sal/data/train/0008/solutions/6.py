for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    inp = input().lower()
    k = min(k, inp.count('l'))
    ans = inp.count('w') + tuple(zip(inp, 'l' + inp)).count('ww') + k * 2
    if 'w' in inp:
        inp2 = []
        cur = -1
        for c in inp:
            if cur != -1:
                if c == 'l':
                    cur += 1
                else:
                    inp2.append(cur)
            if c == 'w':
                cur = 0
        inp2.sort()
        for inp2i in inp2:
            if inp2i > k:
                break
            k -= inp2i
            ans += 1
    else:
        ans = max(ans - 1, 0)
    print(ans)

