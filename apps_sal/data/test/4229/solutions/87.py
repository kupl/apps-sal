n = int(input())
n3 = n // 3

n5 = n // 5
n15 = n // 15

ans = (n + 1) * n // 2 - (3 + 3 * n3) * n3 // 2 - (5 + 5 * n5) * n5 // 2 + (15 + 15 * n15) * n15 // 2

print(ans)
