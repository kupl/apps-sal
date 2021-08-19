n = int(input())
a = list(map(int, input().split()))
cnt = [1 for x in a if x < 0]
ans = 0
mini = float('inf')
for i in a:
    if i < 0:
        i *= -1
    mini = min(mini, i)
    ans += i
if sum(cnt) % 2 == 0:
    print(ans)
else:
    print(ans - mini * 2)
