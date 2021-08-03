n, x, y = list(map(int, input().split()))
l = list(map(int, input().split()))

for i in range(n):
    if min(l[max(0, i - x):i] + [l[i] + 1]) > l[i] < min(l[i + 1: min(n, i + y + 1)] + [l[i] + 1]):
        print(i + 1)
        break
