N = int(input())
height = list(map(int, input().split()))
for i in range(N - 1, 0, -1):
    n = height[i] - height[i - 1]
    if n <= -2:
        print("No")
        return
    elif n == -1:
        height[i - 1] -= 1
print("Yes")
