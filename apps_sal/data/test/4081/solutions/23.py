n = int(input())
row = list(map(int, input().split()))
l = 0
r = n - 1
last = 0
ans = ''
while 1:

    if row[l] < row[r]:
        if row[l] > last:
            ans += 'L'
            last = row[l]
            l += 1
        elif row[r] > last:
            ans += 'R'
            last = row[r]
            r -= 1
        else:
            break
    else:
        if row[r] > last:
            ans += 'R'
            last = row[r]
            r -= 1
        elif row[l] > last:
            ans += 'L'
            last = row[l]
            l += 1
        else:
            break

print(len(ans))
print(ans)
