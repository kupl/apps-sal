'''input
3
0 0
0 0
0 0

3
2 0
3 1
3 4


'''
n = int(input())
ans = 1
la = lb = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    if max(la, lb) <= min(a, b):
        ans += min(a, b) - max(la, lb) + 1 - (la == lb)
    la, lb = a, b

print(ans)
