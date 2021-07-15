n = int(input())
flag = 0

for i in range(1,9000*18 + 1):

    if (-i + (i**2 + 4*n)**(1/2))/2 == int((-i + (i**2 + 4*n)**(1/2))/2):
      c = int((-i + (i**2 + 4*n)**(1/2))/2)
      if sum(list(map(int,list(str(c))))) == i:
        if c**2 + c*i - n == 0:
          print(int((-i + (i**2 + 4*n)**(1/2))/2))


          flag = 1
          break
if flag == 0:
    print(-1)


