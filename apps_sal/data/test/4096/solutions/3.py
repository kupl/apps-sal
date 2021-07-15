n, m = map(int, input().split())
coffees = sorted(map(int, input().split()), reverse=True)
total = sum(coffees)

if total < m:
    print(-1)
    return

for div in range(1, n):
    a = [0] * div
    index = 0
    for pena in range(n):
        for d in range(div):
            if coffees[index] <= pena:
                break
            a[d] += coffees[index] - pena
            index += 1

            if index >= n or coffees[index] <= pena:
                break
        if index >= n or coffees[index] <= pena:
            break

    if sum(a) >= m:
        print(div)
        return

print(n)
