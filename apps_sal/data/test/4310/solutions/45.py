A = list(map(int, input().split()))
A.sort(reverse=True)
cur = A.pop(0)
ans = 0
for a in A:
    ans += cur - a
    cur = a
print(ans)
