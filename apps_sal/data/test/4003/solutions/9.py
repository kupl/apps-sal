n = int(input())
a = [int(i) for i in input().split()]
last = -1
i = 0
j = n - 1
ans = ''
while i <= j:
    if max(a[i], a[j]) <= last:
        break
    if a[i] == a[j]:
        start = i
        k = 0
        last = a[i]
        i += 1
        while i <= j:
            if a[i] <= last:
                break
            else:
                last = a[i]
                k += 1
                i += 1
        last = a[j]
        k2 = 0
        i = start
        j -= 1
        while i <= j:
            if a[j] <= last:
                break
            else:
                last = a[j]
                k2 += 1
                j -= 1
        if k > k2:
            ans += 'L' * (k + 1)
        else:
            ans += 'R' * (k2 + 1)
        break
    if a[i] < a[j]:
        if a[i] > last:
            ans += 'L'
            last = a[i]
            i += 1
        else:
            ans += 'R'
            last = a[j]
            j -= 1
    else:
        if a[j] > last:
            ans += 'R'
            last = a[j]
            j -= 1
        else:
            ans += 'L'
            last = a[i]
            i += 1
print(len(ans))
print(ans)
