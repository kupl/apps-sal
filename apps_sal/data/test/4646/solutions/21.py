def help():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    ev = []
    od = []
    for i in range(n):
        if arr[i] % 2 == 1:
            if arr[i] % 2 != i % 2:
                od.append(i)
        elif arr[i] % 2 != i % 2:
            ev.append(i)
    if len(ev) == len(od):
        print(len(ev))
    else:
        print(-1)


for _ in range(int(input())):
    help()
