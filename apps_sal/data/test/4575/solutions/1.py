N = int(input())
(D, X) = list(map(int, input().split()))
con = 0
for i in range(N):
    a = int(input())
    if a != 1:
        for i in range(1, D + 1):
            if i % a == 1:
                con += 1
    elif a == 1:
        con += D
print(X + con)
