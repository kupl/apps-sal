N = int(input())
D = list(map(int, input().split()))
sort = sorted(D)
left = sort[(N // 2) - 1]
right = sort[N // 2]
print((right - left))
