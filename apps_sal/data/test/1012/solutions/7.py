n = int(input())
for i in range(n):
    s = input()
    arr = sorted(s)
    if arr[0] == arr[-1]:
        print(-1)
    else:
        print(''.join(arr))
