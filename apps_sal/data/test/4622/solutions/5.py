N = int(input())
A = list(map(int, input().split()))

ans = "NO"
if N == len(set(A)):
    ans = "YES"

print(ans)
