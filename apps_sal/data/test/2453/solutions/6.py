n = int(input())
left = []
right = []
for i in range(n):
    data = input().split()
    left.append(int(data[0]))
    right.append(int(data[1]))

left.sort()
right.sort()
i = 0
j = 0
count = 1
ans = [0] * (n + 1)
left += [max(right) + 1]
right += [max(right) + 2]
while (i < n) and (j < n):
    while left[i + 1] <= right[j]:
        ans[count] += (left[i + 1] - left[i])
        count += 1
        i += 1
    ans[count] += (right[j] - left[i] + 1)
    i += 1
    count -= 1

    while ((i == n) or (right[j + 1] < left[i])) and (j < n - 1):
        ans[count] += (right[j + 1] - right[j])
        count -= 1
        j += 1
    ans[count] += (left[i] - right[j] - 1)
    j += 1
    count += 1


for i in range(1, n + 1):
    print(ans[i], end=" ")
print()
