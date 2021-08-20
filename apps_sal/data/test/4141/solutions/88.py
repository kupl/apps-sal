n = int(input())
(*A,) = list(map(int, input().split()))
ans = 'APPROVED'
for a in A:
    if a % 2 == 0 and a % 3 and a % 5:
        ans = 'DENIED'
print(ans)
