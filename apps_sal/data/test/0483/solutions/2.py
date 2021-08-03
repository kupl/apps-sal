n = int(input())
s = input()
l = list(map(int, input().split()))
ans = 10 ** 18
last_r = -1
for i in range(len(l)):
    if s[i] == 'R':
        last_r = i
    else:
        if last_r != -1:
            ans = min(ans, (l[i] - l[last_r]) // 2)
if ans == 10 ** 18:
    print(-1)
else:
    print(ans)
