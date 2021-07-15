MOD = 10 ** 9 + 7

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 1
if N == K:
    for a in A:
        ans = ans * a % MOD
    print(ans)
    return

minus = []
plus = []
for a in A:
    if a < 0:
        minus.append(a)
    else:
        plus.append(a)

if len(minus) == N:
    if K % 2 == 0:
        A.sort()
    else:
        A.sort(reverse=True)
    for i in range(K):
        ans = ans * A[i] % MOD
    print(ans)
    return

minus.sort(reverse=True)
plus.sort()

if  K % 2:
    ans *= plus.pop()

B = []

while len(minus) > 1:
    a = minus.pop()
    b = minus.pop()
    B.append(a * b)

while len(plus) > 1:
    a = plus.pop()
    b = plus.pop()
    B.append(a * b)

B.sort()

for i in range(K // 2):
    ans = ans * B.pop() % MOD

print(ans)

