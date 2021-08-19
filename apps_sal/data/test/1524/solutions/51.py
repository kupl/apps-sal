a = list(input())
ans = [0] * len(a)
(even_r, odd_r) = (0, 0)
for i in range(len(a)):
    if a[i] == 'R':
        if i % 2 == 0:
            odd_r += 1
        else:
            even_r += 1
    else:
        if i % 2 == 0:
            ans[i - 1] += even_r
            ans[i] += odd_r
        else:
            ans[i - 1] += odd_r
            ans[i] += even_r
        odd_r = 0
        even_r = 0
(even_l, odd_l) = (0, 0)
for i in range(len(a) - 1, -1, -1):
    if a[i] == 'L':
        if i % 2 == 0:
            odd_l += 1
        else:
            even_l += 1
    else:
        if i % 2 == 0:
            ans[i + 1] += even_l
            ans[i] += odd_l
        else:
            ans[i + 1] += odd_l
            ans[i] += even_l
        odd_l = 0
        even_l = 0
print(' '.join(list(map(str, ans))))
