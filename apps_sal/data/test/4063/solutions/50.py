N = int(input())
D = list(map(int, input().split()))
D.sort()
left = D[N // 2 - 1]
right = D[N // 2]
print(right - left)
