n, k = list(map(int, input().split()))
x = [int(i) for i in input().split()]
current = x[0]
left_index = 0
right_index = 0
pe = True
count = 1
while (x[left_index] + k < x[-1]):
    while (x[right_index] <= x[left_index] + k):
        right_index += 1
    right_index -= 1
    count += 1
    if (count > n):
        count = -1
        break
    left_index = right_index
print(count)
