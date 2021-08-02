MOD = 10 ** 9 + 7
num = [0] * (10 ** 5 + 1)
N = int(input())
A = list(map(int, input().split()))
for i in range(len(A)):
    num[A[i]] += 1
if N % 2 == 1:
    for i in range(0, N, 2):
        cnt = num[i]
        if i == 0:
            if cnt != 1:
                print(0)
                return
        else:
            if cnt != 2:
                print(0)
                return
    print(2 ** (N // 2) % MOD)
else:
    for i in range(1, N, 2):
        cnt = num[i]
        if cnt != 2:
            print(0)
            return
    print(2 ** (N // 2) % MOD)
