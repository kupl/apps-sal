n, k = [int(i) for i in input().split(' ')]
a = sorted([int(i) for i in input().split(' ')])

if n == 1:
    print(0)
    return
tot = 0
i, j = 1, n - 2

while j - i >= -1:
    do = i > (n - j - 1)

    last = tot
    tot += i * (a[i] - a[i - 1]) if not do else (n - j - 1) * (a[j + 1] - a[j])

    if tot >= k:

        if do:
            a[-1] -= (k - last) // (n - j - 1)
        else:
            a[0] += (k - last) // i
        break

    if do:
        a[-1] = a[j]
        j -= 1
    else:
        a[0] = a[i]
        i += 1

print(a[-1] - a[0])
