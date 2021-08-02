
a, b, c = list(map(int, input().split()))

a %= b

visited = set()

result = -1
i = 1

while True:
    if a * 10 in visited:
        break
    visited.add(a * 10)
    tmp = (a * 10) // b
    if tmp == c:
        result = i
        break
    a = (a * 10) % b
    i += 1


print(result)
