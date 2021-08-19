# A

n = int(input())
min1, max1 = list(map(int, input().split()))
min2, max2 = list(map(int, input().split()))
min3, max3 = list(map(int, input().split()))

x = n - min1 - min2 - min3

ans1 = min(max1, x + min1)
x = x - (ans1 - min1)

ans2 = min(max2, x + min2)
x = x - (ans2 - min2)

ans3 = min3 + x
print(ans1, ans2, ans3)
