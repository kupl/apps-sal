x, y = map(int, input().split())

arr = [x]

while arr[-1] <= y:
    arr.append(arr[-1] * 2)
arr.pop()

print(len(arr))
