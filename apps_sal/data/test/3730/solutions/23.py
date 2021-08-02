n = int(input())
a = [int(x) for x in input().split()]

l, r = 0, 0
c = None
mx = 1

while r < n - 1:
    r += 1

    if a[r] <= (a[r - 1] if r - 1 != c else a[r - 2] + 1):
        if c is not None and r - 1 == c and a[r - 1] < a[r]:
            if a[c] < a[c + 1]:
                l = c = c - 1
            else:
                l = c
        else:
            if c is not None:
                if a[c] < a[c + 1]:
                    l = c
                else:
                    l = c + 1

            if r - 1 == l or a[r] - a[r - 2] > 1:
                c = r - 1
            else:
                c = r

    mx = max(mx, r - l + 1)

print(mx)
