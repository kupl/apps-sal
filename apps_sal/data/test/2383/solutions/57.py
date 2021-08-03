N = int(input())
lsa = list(map(int, input().split()))
a = 1
for i in range(N):
    if lsa[i] == a:
        a += 1
if a == 1:
    ans = -1
else:
    ans = N - (a - 1)
print(ans)
