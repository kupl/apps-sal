n, bx = list(map(int, input().split()))
x = list(map(int, input().split()))
m, by = list(map(int, input().split()))
y = list(map(int, input().split()))
tmp = 1
ans = 0
for i in range(1, n + 1):
    ans += x[-i] * tmp
    tmp *= bx
ans1 = 0
tmp = 1
for i in range(1, m + 1):
    ans1 += y[-i] * tmp
    tmp *= by
if ans < ans1:
    print("<")
elif ans > ans1:
    print(">")
else:
    print("=")
