a = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
for i in range(a):
    if b[i] > c[i]:
        ans += b[i] - c[i]
print(ans)
