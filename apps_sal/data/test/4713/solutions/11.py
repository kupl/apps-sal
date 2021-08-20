n = int(input())
s = input()
(x, ans) = (0, 0)
for o in s:
    if o == 'I':
        x += 1
    else:
        x -= 1
    ans = max(ans, x)
print(ans)
