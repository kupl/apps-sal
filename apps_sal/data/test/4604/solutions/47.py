n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
num = 0
judge = 0
if len(a) % 2 == 1:
    if a[0] == 0:
        for i in range(1, n, 2):
            if a[i] == i + 1 and a[i + 1] == i + 1:
                num += 1
            else:
                print(0)
                judge = 1
                break
    else:
        print(0)
        judge = 1
else:
    for i in range(0, n, 2):
        if a[i] == i + 1 and a[i + 1] == i + 1:
            num += 1
        else:
            print(0)
            judge = 1
            break
if judge == 0:
    result = 2 ** num % (10 ** 9 + 7)
    print(result)
