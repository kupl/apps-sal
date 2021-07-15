A, B, C = map(int, input().split())

n = A*(A+1)//2 * B*(B+1)//2 * C*(C+1)//2
ans = n % 998244353

print(ans)
