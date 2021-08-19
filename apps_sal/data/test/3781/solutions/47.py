T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    if N % 2 == 1:
        print('Second')
    else:
        a.sort()
        for i in range(N // 2):
            if a[2 * i] != a[2 * i + 1]:
                print('First')
                break
        else:
            print('Second')
