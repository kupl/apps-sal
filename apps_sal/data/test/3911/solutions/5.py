n = int(input())
arr = [1]
for i in range(1, n):
    arr.append(1)
    while len(arr) > 1 and arr[-1] == arr[-2]:
        arr.pop()
        arr[-1] += 1
print(*arr)
