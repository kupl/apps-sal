n = int(input())
a = sorted(map(int, input().split()))
res = [10 ** 18]
i = 0
j = n - 1
step = 0
while i <= j:
    if step == 0:
        res.append(a[i])
        i += 1
        if res[-1] > res[-2]:
            print('Impossible')
            break
    else:
        res.append(a[j])
        j -= 1
        if res[-1] < res[-2]:
            print('Impossible')
            break
    step = step ^ 1
else:
    print(' '.join(map(str, res[1:])))
