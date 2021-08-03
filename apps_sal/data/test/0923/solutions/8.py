n = int(input())
arr = [int(x) for x in input().split()]

for _ in range(n + 7):

    for i in range(n):
        if i % 2 == 0:
            arr[i] += 1
            arr[i] %= n
        else:
            arr[i] -= 1
            if arr[i] == -1:
                arr[i] = n - 1

    # print(arr)

    okay = True
    for i in range(n):
        if i != arr[i]:
            okay = False
            break

    if okay:
        print('Yes')
        return

print('No')
