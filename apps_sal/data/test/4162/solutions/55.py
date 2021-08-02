n = int(input())
a = list(map(int, input().split()))
ans = 0
ANS = 0
for i in range(n):
    ans *= a[i]
ans -= 1
for i in range(n):
    ANS += ans % a[i]
print(ANS)
