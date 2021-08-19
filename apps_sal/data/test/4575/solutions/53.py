N = int(input())
(D, Z) = map(int, input().split())
cnt = N
for i in range(N):
    A = int(input())
    day = 1 + A
    while day <= D:
        cnt += 1
        day += A
print(cnt + Z)
