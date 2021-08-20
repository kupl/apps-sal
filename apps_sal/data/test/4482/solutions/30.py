n = int(input())
a = [int(x) for x in input().split()]
A = min(a)
B = max(a)
temp = 10000000000000000000000
for i in range(A, B + 1):
    ans = 0
    for j in a:
        ans += abs(j - i) ** 2
    temp = min(temp, ans)
print(temp)
