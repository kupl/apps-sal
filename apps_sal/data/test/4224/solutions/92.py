N = int(input())
a = list(map(int, input().split()))


def get_divisible_count(x: int) -> int:
    divisible_count = 0
    while x % 2 == 0:
        divisible_count += 1
        x /= 2
    return divisible_count


ans = 0
for n in range(N):
    ans += get_divisible_count(a[n])
print(ans)
