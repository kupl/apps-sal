N = int(input())
A = [tuple(int(j) for j in input().split()) for i in range(N)]
S1, S2 = 0, 0

for a, b in A:
    S1 += a
    S2 += b

if S1 % 2 == 0 and S2 % 2 == 0:
    print(0)
    return

if (S1 % 2 == 0) ^ (S2 % 2 == 0):
    print(-1)
    return

for a, b in A:
    if (a % 2 == 0) ^ (b % 2 == 0):
        print(1)
        return

print(-1)
