n = int(input())
a = list(map(int, input().split()))


def count_2(x, num):
    if x % 2 == 0:
        return count_2(x // 2, num + 1)
    else:
        return num


ans = 0
for i in range(n):
    ans += count_2(a[i], 0)

print(ans)
