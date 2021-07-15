def solve(n):
  start = 1
  end = n*n
  halfN = n // 2
  while(n):
    line = ""
    i=0
    while(i<halfN):
      line += str(start) + " "
      start += 1
      i += 1
    i=0
    while(i<halfN):
      line += str(end) + " "
      end -= 1
      i += 1
    n -= 1
    print(line)

n = int(input())

solve(n)
