n = int(input())
m = int(input())
L = []
for i in range(n):
    L.append(int(input()))
L.sort()
ans = 0
while m > 0:
    ans += 1
    m -= L.pop()
print(ans)
