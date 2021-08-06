n = int(input())
a = list(map(int, input().split()))

odd, even = a[::2], a[1::2]

if n % 2 == 0:
    ans = even[::-1] + odd
else:
    ans = odd[::-1] + even

print(*ans)
