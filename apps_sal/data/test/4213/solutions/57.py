N = int(input())
A = list(map(int, input().split()))
Amax = max(A)
Amin = min(A)
ans = Amax - Amin
print(ans)
