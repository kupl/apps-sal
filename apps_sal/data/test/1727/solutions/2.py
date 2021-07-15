n = int(input())
x = [0] * (n + 1)
h = [0] * (n + 1)

for i in range(n):
    x[i], h[i] = (int(c) for c in input().split())

h[n] = 1
x[n] = x[n-1] + h[n-1] + 1

if n == 1:
    print(1)
    return

left = [0] * n
right = [0] * n

left[0] = 1
if x[0] + h[0] < x[1]:
    right[0] = 1

for i in range(1, n):
    if x[i] + h[i] < x[i + 1]:
        right[i] = max(right[i-1], left[i-1]) + 1
    else:
        right[i] = max(right[i-1], left[i-1])

    if x[i] - h[i] > x[i-1] + h[i-1]:
        left[i] = max(right[i-1], left[i-1]) + 1
    elif x[i] - h[i] > x[i-1]:
        left[i] = left[i-1] + 1
    else:
        left[i] = max(right[i-1], left[i-1])

print(max(left[n-1], right[n-1]))
