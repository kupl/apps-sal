"""Boot-camp-for-Beginners_Easy009_B_Collecting-Balls-(Easy-Version)_28-August-2020.py"""
N = int(input())
K = int(input())
x = list(map(int, input().split()))
s = 0
for i in range(N):
    if x[i] < K / 2:
        s += 2 * x[i]
    else:
        s += 2 * (K - x[i])
print(s)
