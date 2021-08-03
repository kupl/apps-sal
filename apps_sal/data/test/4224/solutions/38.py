n = int(input())
a = list(map(int, input().split()))


def count_2(x):
    if x % 2 != 0:
        return 0
    else:
        return count_2(x // 2) + 1


ans = 0
for i in range(n):
    ans += count_2(a[i])

print(ans)
