N = int(input())
A = list(map(int, input().split()))
l = 1
s = 0
for i in A:
    if i == l:
        l += 1
if l == 1:
    ans = -1
else:
    ans = N - l + 1
print(ans)
