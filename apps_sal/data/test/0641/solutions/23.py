inp = input().split()
if inp[2] == 'week':
    ans = 51
    if inp[0] in '567':
        ans += 1
    if inp[0] in '123456':
        ans += 1
    print(ans)
else:
    x = int(inp[0])
    ans = 7
    if x <= 29:
        ans += 1
    if x <= 30:
        ans += 4
    print(ans)
