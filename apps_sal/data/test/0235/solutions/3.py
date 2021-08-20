def how_much_he_eats(n, k):
    result = 0
    while n != 0:
        eats = min([n, k])
        result += eats
        n -= eats
        n -= n // 10
    return result


n = int(input())
(a, b, c) = (1, n, 0)
while a < b:
    c = (a + b) // 2
    if 2 * how_much_he_eats(n, c) >= n:
        b = c
    else:
        a = c + 1
print(a)
