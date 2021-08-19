N = int(input())
aaa = list(map(int, input().split()))
M = 0
bbb = [0] * (N + 1)
for i in range(N, 0, -1):
    if (aaa[i - 1] + sum(bbb[i::i])) % 2 == 1:
        M += 1
        bbb[i] = 1
print(M)
if M > 0:
    ans = [i for i, b in enumerate(bbb) if b]
    print((*ans))
