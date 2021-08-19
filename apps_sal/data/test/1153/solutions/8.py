(n, m) = list(map(int, input().split()))
xi = list(map(int, input().split()))
yi = list(map(int, input().split()))
i = 0
j = 0
ans = 0
x = xi[0]
y = yi[0]
while n > i and m > j:
    if x == y:
        ans += 1
        i += 1
        j += 1
        if n <= i or m <= j:
            break
        x = xi[i]
        y = yi[j]
    elif x > y:
        j += 1
        if m <= j:
            break
        y += yi[j]
    else:
        i += 1
        if n <= i:
            break
        x += xi[i]
print(ans)
