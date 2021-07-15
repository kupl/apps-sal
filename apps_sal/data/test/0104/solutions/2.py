def inpmap():
    return list(map(int, input().split()))
n = int(input())
arr = list(inpmap())
s = sum(arr)
a = 0
for i in range(n):
    a += arr[i]
    if a >= s / 2:
        print(i + 1)
        break

