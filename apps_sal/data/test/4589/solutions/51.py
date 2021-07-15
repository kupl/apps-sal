H, W = map(int, input().split())
L = ['.' + input() + '.' for _ in range(H)]
L = ['.' * (W + 2)] + L + ['.' * (W + 2)]
A = []
for i in range(1, H + 1):
  S = ""
  for j in range(1, W + 1):
    if L[i][j] == '.':
      t = [L[i-1][j-1], L[i-1][j], L[i-1][j+1], L[i][j+1], L[i+1][j+1], L[i+1][j], L[i+1][j-1], L[i][j-1]]
      S += str(t.count('#'))
    else:
      S += '#'
  A.append(S)
[print(i) for i in A]
