n = int(input())
cnt1 = 1
cnt2 = n ** 2
arr = []
for i in range(n * n // 2):
    arr.append([cnt1, cnt2])
    cnt1 += 1
    cnt2 -= 1
for i in range(0, len(arr), n // 2):
    for j in range(n // 2):
        print(arr[i + j][0], arr[i + j][1], sep=' ', end=' ')
    print('')
