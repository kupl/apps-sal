n = int(input())
a = ["x" * (n + 2)] + ["x" + input() + "x" for i in range(n)] + ["x" * (n + 2)]
def f(i, j):
  c = 0
  if a[i - 1][j] == 'o':
    c += 1
  if a[i][j - 1] == 'o':
    c += 1
  if a[i + 1][j] == 'o':
    c += 1
  if a[i][j + 1] == 'o':
    c += 1
  return c % 2 == 0
print("YES" if all(f(i + 1, j + 1) for i in range(n) for j in range(n)) else "NO")
