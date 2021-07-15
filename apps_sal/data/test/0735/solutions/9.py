def reverse(arr, left, right):
    while left < right:
        t = arr[left]
        arr[left] = arr[right]
        arr[right] = t
        left += 1
        right -= 1

n = int(input())
a = list(map(int, input().split()))
b = a.copy()
b.sort()
left = -1
right = -1
for i in range(n):
    if a[i] != b[i]:
        left = i
        break
if left == -1:
    print("yes")
    print(1, 1)
    return
for i in range(n - 1, -1, -1):
    if a[i] != b[i]:
        right = i
        break
reverse(a, left, right)
for i in range(n):
    if a[i] != b[i]:
        print("no")
        return
print("yes")
print(left + 1, right + 1)

