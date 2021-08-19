n, a, b = [int(x) for x in input().split()]
if a * b < n or n < a + b - 1:
    print((-1))
else:
    ans = []
    remaining = n - a
    to_insert = 1
    for i in range(a):
        ans.append(to_insert)
        to_insert += 1
        inserted = 1
        for j in range(min(b - 1, remaining)):
            ans.append(to_insert)
            to_insert += 1
            inserted += 1
            remaining -= 1
        ans[-inserted:] = reversed(ans[-inserted:])
    print((*ans))
