a = input()
b = input()
diff = 0
for i in range(len(a)):
    if a[i] != b[i]:
        diff += 1
if diff % 2 != 0:
    print('impossible')
else:
    start = 0
    ans = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            if start % 2 == 0:
                ans += a[i]
            elif start % 2 == 1:
                ans += b[i]
            start += 1
        else:
            ans += a[i]
    print(ans)
