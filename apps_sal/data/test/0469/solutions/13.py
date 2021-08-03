r, h = list(map(int, input().split()))

a = 2 * (h // r)

h = h % r

print(a + 1 + (2 * h >= r) + (4 * h * h >= 3 * r * r))


# Made By Mostafa_Khaled
