n = int(input())
ANS = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    if x + y > ANS:
        ANS = x + y

print(ANS)
