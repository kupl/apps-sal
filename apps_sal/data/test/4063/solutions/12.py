N = int(input())
D = sorted(list(map(int, input().split())))

left = D[N // 2 - 1]
right = D[N // 2]

print(right - left)
