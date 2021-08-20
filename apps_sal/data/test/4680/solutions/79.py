A = list(map(int, input().split()))
ans = 'NO'
if A.count(5) == 2 and A.count(7) == 1:
    ans = 'YES'
print(ans)
