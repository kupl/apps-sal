(m, k) = list(map(int, input().split()))
if m == 1 and k == 1:
    print(-1)
elif m == 1 and k == 0:
    print('0 0 1 1')
elif 2 ** m > k:
    ans = str(k)
    y = []
    for i in range(2 ** m):
        if i == k:
            continue
        y.append(str(i))
    ans = ' '.join(reversed(y)) + ' ' + ans + ' ' + ' '.join(y) + ' ' + ans
    print(ans)
else:
    print(-1)
