n = int(input())
a = list(map(int, input().split()))
our = a[0]
ans = [1]
for i in range(1, n):
    if a[i] * 2 <= a[0]:
        our += a[i]
        ans.append(i + 1)
if our > sum(a) - our:
    print(len(ans))
    print(*ans)
else:
    print(0)
