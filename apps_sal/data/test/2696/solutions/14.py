n = int(input())
arr = list(map(int, input().split()))
for i in range(n - 1, 0, -1):
    if arr[i] == arr[i - 1]:
        pass
    else:
        print(i + 1)
        break
else:
    print(1)
