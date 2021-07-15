n = int(input())
xs = list(map(int, input().split()))

xs.sort(reverse=True)

a = xs[0]
b = xs[1]

for i in xs[2:]:
    if a + i - b > b + i - a:
        b += i
    else:
        a += i

print(abs(a - b) + 1)

