n = int(input())
arr = [1, 8, 4, 2, 6]
if n == 0:
    print(1)
elif n % 4 == 0:
    print(6)
else:
    print(arr[n % 4])
