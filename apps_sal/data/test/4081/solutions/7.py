n = int(input())
a = [int(i) for i in input().split()]
last = -1
i = 0
j = n - 1
ans = ''
while i <= j:
    if max(a[i], a[j]) <= last:
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

