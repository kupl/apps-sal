a, b = map(int, input().split())
if min(a, b) >= 3:
    print((a - 2) * (b - 2))
    return
if a > b:
    a, b = b, a
if a == 1 and b >= 3:
    print(b - 2)
if a == 2 and b >= 3:
    print(0)


if [a, b] == [1, 1]:
    print(1)
if [a, b] == [1, 2]:
    print(0)
if [a, b] == [2, 2]:
    print(0)
