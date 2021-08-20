__author__ = 'Данила'
n = int(input())
(min1, max1) = list(map(int, input().split()))
(min2, max2) = list(map(int, input().split()))
(min3, max3) = list(map(int, input().split()))
ans1 = min(max1, n - min2 - min3)
n -= ans1
ans2 = min(max2, n - min3)
ans3 = n - ans2
print(ans1, ans2, ans3)
