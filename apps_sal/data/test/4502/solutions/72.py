n = int(input())
a = list(map(int, input().split()))

odd_index = []
even_index = []
for i in range(n):
    if (i + 1) % 2 == 1:
        odd_index.append(a[i])
    else:
        even_index.append(a[i])

if n % 2 == 1:
    res = odd_index[::-1] + even_index
else:
    res = even_index[::-1] + odd_index

print((*res))

