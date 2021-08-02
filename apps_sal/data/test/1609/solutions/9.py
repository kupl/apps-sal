n = int(input())
pin = input().split(" ")
arr = [int(i) - 1 for i in pin]
free = [True] * n
change = []
for i in range(n):
    if arr[i] < n:
        if free[arr[i]]:
            free[arr[i]] = False
        else:
            change.append(i)
    else:
        change.append(i)

for i in range(n):
    if free[i]:
        arr[change.pop()] = i

for i in arr:
    print(i + 1, end=" ")
