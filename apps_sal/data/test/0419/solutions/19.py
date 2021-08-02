s = input()
ans = (len(s) + 1) // 2
if len(s) % 2 == 1 and s[1:] == '0' * (len(s) - 1):
    ans -= 1
print(ans)
