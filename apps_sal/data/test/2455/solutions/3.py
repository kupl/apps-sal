t = int(input())
for i in range(t):
    s = input().strip()
    cnt = 0
    ans = []
    for b in [1, 2, 3, 4, 6, 12]:
        List = []
        a = 12 // b
        for begin in range(b):
            column = ''
            j = begin
            while j < 12:
                column += s[j]
                j += b
            List.append(column)
        if 'X' * a in List:
            cnt += 1
            ans.append((a, b))
    print(cnt, end=' ')
    for pair in sorted(ans):
        print('x'.join(map(str, pair)), end=' ')
    print()
