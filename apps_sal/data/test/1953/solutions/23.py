t = int(input())
A = list(map(int, input().split()))
s = 0
ans = 0
x = 0
A.sort()
while x < t:
    if s <= A[x]:
        ans += 1
        s += A[x]
    x += 1
print(ans)
