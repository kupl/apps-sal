N = int(input())
a = list(map(int, input().split()))

a.sort()
a.reverse()

c = [0, 0]
i = 0

while i < N - 1:
    if a[i] == a[i + 1]:
        c.append(a[i])
        i += 2
    else:
        i += 1

c.sort()
c.reverse()
print(c[0] * c[1])
