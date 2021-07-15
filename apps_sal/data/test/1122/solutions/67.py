n, m = list(map(int, input().split()))

even = m // 2
odd = m - even

odd_left = 1
odd_right = 2 * odd

even_left = odd_right + 1
even_right = even_left + 2 * even

for _ in range(odd):
    print((odd_left, odd_right))
    odd_left += 1
    odd_right -= 1

for _ in range(even):
    print((even_left, even_right))
    even_left += 1
    even_right -= 1

