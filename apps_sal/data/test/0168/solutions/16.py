N = int(input())
s = input()
ans = 0
for i in range(N):
    if s[i] == '-':
        ans -= 1
    else:
        ans += 1
    if ans < 0:
        ans = 0
print(ans)
