n, k = map(int, input().split())
a = [i - 1 for i in map(int, input().split())]

left, right = 1, 10**9
while left < right:
    middle = (left + right) // 2

    count = 0
    for i in a:
        count += i // middle

    if count <= k:
        right = middle
    else:
        left = middle + 1

print(left)
