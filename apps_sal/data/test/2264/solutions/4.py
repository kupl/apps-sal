t = int(input())
for T in range(t):
    n = int(input())
    arr = [tuple(map(int, input().split())) for i in range(n)]

    arr.sort(key=lambda x: x[1])
    a = arr[0][1]
    arr.sort(key=lambda x: -x[0])
    b = arr[0][0]

    if a <= b:
        print(b - a)
    else:
        print(0)
