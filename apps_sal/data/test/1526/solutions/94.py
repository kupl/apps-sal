a, b, c = list(map(int, input().split()))
ma = max(a, b, c)
ans = ((ma - a) // 2) + ((ma - b) // 2) + ((ma - c) // 2)
a = 2 * ((ma - a) // 2) + a
b = 2 * ((ma - b) // 2) + b
c = 2 * ((ma - c) // 2) + c

ma = max(a, b, c)
cnt0 = 0
sa = [ma - a, ma - b, ma - c]
for i in sa:
    if i == 0:
        cnt0 += 1

if cnt0 == 3:
    print(ans)
elif cnt0 == 2:
    print((ans + 2))
elif cnt0 == 1:
    print((ans + 1))
