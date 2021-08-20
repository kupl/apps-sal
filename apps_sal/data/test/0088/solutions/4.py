(x, y) = list(map(int, input().split()))
ans = 0
for left in range(1, 100):
    s = '1' * left + '0'
    for right in range(100):
        a = int(s, 2)
        if a > y:
            break
        if a >= x:
            ans += 1
        s += '1'
print(ans)
