input()
s = input()

ans = 0
if len(s) > 26:
    print(-1)
    quit()

for let in 'abcdefghijklmnopqrstuvwxyz':
    ans += max(0, s.count(let) - 1)

print(ans)
