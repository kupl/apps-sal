n = int(input())
s = input()
ans = 0
sc, gc, pi, ci = 0, 0, -1, -1
for i in range(1, n + 1):
    if s[i - 1] == 'G':
        gc += 1
    else:
        sc += 1
        if pi == -1:
            ans = max(ans, i - 1)
        else:
            ans = max(ans, i - 1 - pi)
        pi = ci
        ci = i
    # print(ans)
# print(gc,sc)
if sc == 1:
    print(n - 1)
    return
if sc == 2 and (s[0] == 'S' or s[n - 1] == 'S'):
    print(n - 2)
    return

if pi == -1:
    ans = max(ans, n)
else:
    ans = max(ans, n - pi)

print(min(ans, gc))
