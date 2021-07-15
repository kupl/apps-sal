N, M = list(map(int, input().split()))
odd_l = 1
odd_r = M
even_l = M + 1
even_r = 2 * M + 1
i = 0
while i < M:
    print((even_l, even_r))
    i += 1
    if i == M:
        break
    print((odd_l, odd_r))
    i += 1
    odd_l += 1
    odd_r -= 1
    even_l += 1
    even_r -= 1

