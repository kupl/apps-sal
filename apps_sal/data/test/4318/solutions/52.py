n = int(input())
list_h = [int(i) for i in input().split()]
count = 0
max = 0
for i in range(0, n):
    if list_h[i] >= max:
        count += 1
        max = list_h[i]
print(count)
