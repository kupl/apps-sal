A, B, K = map(int, input().split())

num = []
if A == B:
    print(A)
elif (B + 1 - A) / 2 <= K:
    for i in range(A, B + 1):
        print(i)
else:
    for j in range(K):
        num.append(A + j)
        num.append(B - j)
    for k in range(len(num)):
        num.sort()
        print(num[k])
