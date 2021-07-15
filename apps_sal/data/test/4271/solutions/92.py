n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
x = -1

for i in A:
    ans += B[i-1]
    if x+1 == i:
        ans += C[x-1]
    x = i

print(ans)


