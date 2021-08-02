n, x, y = list(map(int, input().split()))
a = [int(e) for e in input().split()]
if x > y:
    print(n)
    return
cnt = 0
for i in a:
    if i <= x:
        cnt += 1
print((cnt + 1) // 2)
