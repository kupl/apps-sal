(n, k) = map(int, input().split())
s = input()
rl = 0
end = 0
if s[0] == 'L':
    end += 1
if s[-1] == 'R':
    end += 1
for i in range(n - 1):
    if s[i] == 'R' and s[i + 1] == 'L':
        rl += 1
ans = n - 2 * rl - end
if end == 0:
    if k >= rl:
        ans += 2 * rl
        ans -= 1
    else:
        ans += 2 * k
elif end == 1:
    if k >= rl:
        ans += 2 * rl
    else:
        ans += 2 * k
elif end == 2:
    if k == rl:
        ans += 2 * rl
    elif k >= rl + 1:
        ans += 2 * rl
        ans += 1
    else:
        ans += 2 * k
print(ans)
