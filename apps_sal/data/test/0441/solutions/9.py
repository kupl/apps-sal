(n, a, b) = list(map(int, input().split()))

lst = list(input())

k = 0
array = []
for x in range(n):
    if lst[x] == '*':
        array.append(k)
        k = 0
    else:
        k += 1

if lst[0] == '*':
    array = array[1:]
if lst[-1] != '*':
    array.append(k)

s = a + b
for x in array:
    if max(a, b) == a:
        p = (x + 1) // 2
        a = max(a - p, 0)
        b = max(b - (x - p), 0)
    else:
        p = (x + 1) // 2
        b = max(b - p, 0)
        a = max(a - (x - p), 0)

print(s - (a + b))
