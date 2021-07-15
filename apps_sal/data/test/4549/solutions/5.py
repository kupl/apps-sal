h, w = map(int, input().split())
ss = [input() for i in range(h)]
sm = ['.'+s+'.' for s in ss]
mm = ['.'*(w+2)]+sm+['.'*(w+2)]

for i in range(1,h+1):
  for j in range(1,w+1):
    if mm[i][j] == '#' and mm[i][j-1] == '.' and mm[i][j+1] == '.' and mm[i-1][j] =='.' and mm[i+1][j] == '.':
      print('No')
      return


print('Yes')
