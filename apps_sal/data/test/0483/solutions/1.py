n = int(input())
s = input()
x = list(map(int, input().split()))
ans = float('inf')
last = None
for i in range(n):
    if s[i] == 'R':
        last = x[i]
    elif last != None:
        cur = (x[i] - last) // 2
        ans = min(ans, cur)
if ans == float('inf'):
    ans = -1
print(ans)

