n = int(input())
A = list(map(int, input().split()))
num1 = 0
ans = 0
for a in A:
    d = a // 2
    deduct = min(num1, d)
    num1 -= deduct
    ans += deduct
    a -= deduct * 2
    ans += a // 3
    num1 += a % 3
print(ans)
