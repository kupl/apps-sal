from sys import stdin

board = None
deltar = [ -1, 0, 0, 1]
deltac = [ 0, -1, 1, 0]

def main():
  nonlocal board, deltar, deltac
  inp = stdin
  board = [ [ int(x) for x in inp.readline().strip().split() ] for i in range(3) ]
  ans = [ [ 0 for j in range(3) ] for i in range(3) ]
  for r in range(3):
    for c in range(3):
      ans[r][c] += board[r][c]
      for a in range(4):
        if 0<=r+deltar[a]<3 and 0<=c+deltac[a]<3:
          ans[r][c] += board[r+deltar[a]][c+deltac[a]]
  for r in range(3):
    print(''.join(str(1-(ans[r][c]%2)) for c in range(3)))

main()

