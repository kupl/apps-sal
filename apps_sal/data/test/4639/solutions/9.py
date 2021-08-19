t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    opts = 0
    b_pos = n - 2
    while opts + (n - b_pos - 1) < k:
        opts += n - b_pos - 1
        b_pos -= 1
    b_pos2 = n - (k - opts)
    res = ['a'] * n
    res[b_pos] = 'b'
    res[b_pos2] = 'b'
    print(''.join(res))
