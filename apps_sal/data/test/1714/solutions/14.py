n, k = list(map(int, input().split()))

p = [str(i) for i in range(1, 2 *n + 1)]

for i in range(k):

  p[2 * i], p[2 * i + 1] = p[2 * i + 1], p[2 * i]

print(" ".join(p))



# Made By Mostafa_Khaled

