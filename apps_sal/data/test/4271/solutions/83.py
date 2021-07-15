N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
num = 0
for i in A:
    ans += B[i-1]
    if num != 0 and i - num == 1:
        ans += C[i-2]
    num = i
    
print(ans)
