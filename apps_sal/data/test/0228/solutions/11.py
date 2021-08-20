n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
x = 1
while True:
    if arr.count(x) > n // 2:
        print('Bob')
        break
    elif x in arr:
        print('Alice')
        break
    else:
        x += 1
