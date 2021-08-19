def f():
    s = input()
    ans = [0] * len(s)
    i = 0
    cur = 0
    while i < len(s):
        sub = s[i:i + 3]
        if sub == 'one':
            ans[cur] = i + 1 + 1
            i = i + 3
            cur += 1
        elif sub == 'two':
            if s[i + 3:i + 5] == 'ne':
                ans[cur] = i + 2 + 1
                i = i + 5
            else:
                ans[cur] = i + 1 + 1
                i = i + 3
            cur += 1
        else:
            i += 1
    print(cur)
    print(*ans[:cur])


q = int(input())
for _ in range(q):
    f()
