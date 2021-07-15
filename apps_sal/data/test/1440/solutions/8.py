n = int(input())
a = list(map(int, input().split()))

ans = 0
spare = 0

for i in range(n):
    can_build_2 = min(spare, a[i] // 2)
    ans += can_build_2
    spare -= can_build_2
    a[i] -= can_build_2 * 2

    ans += a[i] // 3
    spare += a[i] % 3

print(ans)

