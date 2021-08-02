N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
pre_a = -1

for a in A:
    ans += B[a - 1]
    if a == pre_a + 1:
        ans += C[a - 2]
    pre_a = a

print(ans)
