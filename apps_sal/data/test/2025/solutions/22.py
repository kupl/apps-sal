n = int(input())
ans = ''
for i in range(n):
    a = int(input())
    if a % 2 != 0:
        b = (a - 9) // 4
        if a == 1 or a == 3 or a == 5 or (a == 7) or (a == 11):
            ans += '-1\n'
        else:
            ans += str(b + 1) + '\n'
    else:
        b = a // 4
        if a < 4:
            ans += '-1\n'
        else:
            ans += str(b) + '\n'
print(ans[:-1])
