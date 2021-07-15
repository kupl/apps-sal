n = int(input())
a = list(map(int, input().split()))

max = 0
length = 1

for i in range(1, n):
    if a[i] > a[i-1]:
        length += 1
    else:
        if length > max:
            max = length
        length = 1

if length > max:
    max = length

print(max)

