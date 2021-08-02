N = int(input())
a = list(map(int, input().split()))
if abs(max(a)) >= abs(min(a)):
    for i in range(N):
        if a[i] == max(a):
            num = i
            break
    print(2 * N - 1)
    for i in range(N):
        if num != i:
            print(num + 1, i + 1)
    print(num + 1, num + 1)
    for i in range(1, N):
        print(i, i + 1)
else:
    for i in range(N):
        if a[i] == min(a):
            num = i
            break
    print(2 * N - 1)
    for i in range(N):
        if num != i:
            print(num + 1, i + 1)
    print(num + 1, num + 1)
    for i in range(N - 1):
        print(N - i, N - i - 1)
