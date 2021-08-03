n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))


def avg_tmp(t, x):
    return t - x * 0.006


ans, ans_index = 10000000, 0
for i in range(n):
    if abs(avg_tmp(t, h[i]) - a) < abs(ans - a):
        ans = avg_tmp(t, h[i])
        ans_index = i + 1
print(ans_index)
