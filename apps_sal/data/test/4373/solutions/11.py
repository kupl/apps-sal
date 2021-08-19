n = int(input())
A = list(map(int, input().split()))
A.sort()
ANS = 1
for a in A:
    if a >= ANS:
        ANS += 1
print(ANS - 1)
