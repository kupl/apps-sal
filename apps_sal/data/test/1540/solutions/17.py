R = lambda:list(map(int, input().split()))

n, m, k = R()

a = [list(R()) for _ in range(n)]

b = [0] * n

c = [0] * m

for i in range(k):

  x, y = R()

  b[x - 1] += 1

  c[y - 1] += 1

print(" ".join(map(str, (sum(a[i][j] * c[j] for j in range(m)) - b[i] for i in range(n)))))



# Made By Mostafa_Khaled

