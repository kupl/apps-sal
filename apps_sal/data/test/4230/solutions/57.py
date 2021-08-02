x, n = list(map(int, input().split()))
l = list(map(int, input().split()))
a = 0
ab = 0
for i in range(100):
    if x - i not in l:
        ans = x - i
        a = i + 1
        break
for i in range(100):
    if x + i not in l:
        ansb = x + i
        ab = i + 1
        break
if a > ab:
    print(ansb)
else:
    print(ans)
