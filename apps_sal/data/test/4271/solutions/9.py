n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
for i in range(n):
    num = a[i] - 1
    ans += b[num]

    if i == 0:
        continue
    elif a[i - 1] + 1 == a[i]:
        ans += c[num - 1]

print(ans)
