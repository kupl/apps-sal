t = int(input())
for i in range(t):
    s = input()
    j = 0
    ans = []
    while j < len(s) - 2:
        if s[j:j + 5] == 'twone':
            ans.append(j + 3)
            j += 3
        elif s[j:j + 3] in ('one', 'two'):
            ans.append(j + 2)
        j += 1
    print(len(ans))
    print(*ans)

