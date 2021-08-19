for _ in range(int(input())):
    (n, k) = map(int, input().split())
    s = [*input()]
    t = 0
    ans = ['1'] * n
    for i in range(n):
        if s[i] == '0':
            z = min(k, i - t)
            k -= z
            ans[i - z] = '0'
            t += 1
    print(''.join(ans))
