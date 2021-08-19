n = int(input())
lis = list(map(int, input().split()))
if len(lis) == 1:
    print(lis[0])
else:
    lis.sort()
    a = -lis[0] + lis[-1]
    lis = list(map(abs, lis))
    print(a + sum(lis[1:-1]))
