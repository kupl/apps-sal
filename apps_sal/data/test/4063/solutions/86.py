N = int(input())
D = list(map(int, input().split()))
D.sort()
if D[N // 2 - 1] != D[N // 2]:
    print(D[N // 2] - D[N // 2 - 1])
else:
    print(0)
