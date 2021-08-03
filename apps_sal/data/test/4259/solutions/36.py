K = int(input())
A, B = map(int, input().split())
cnt = 0
for i in range(A, (B + 1)):
    if i % K == 0:
        cnt = 1
        break
print("OK" * cnt + "NG" * (1 - cnt))
