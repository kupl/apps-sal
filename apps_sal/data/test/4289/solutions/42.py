n = int(input())
t, a = (int(i) for i in input().split())
list_h = [int(i) for i in input().split()]
tmp = 999
ans = 0
for i in range(0, n):
    if tmp > abs((t - list_h[i] * 0.006) - a):
        tmp = abs((t - list_h[i] * 0.006) - a)
        ans = i
print(ans + 1)
