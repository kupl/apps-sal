N = int(input())
A = list(map(int, input().split()))
B = [1 / i for i in A]
Bs = sum(B)
ans = 1 / Bs
print(ans)
