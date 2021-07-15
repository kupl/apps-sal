n,d=map(int,input().split())
ch=input()
i=0
l=len(ch)
com=0
while True:
      if len(ch)-i <= d:
            if len(ch)-i>1:
                  com+=1
            print(com)
            break
      else:
            if '1' in ch[i+1:i+d+1]:
                  ch3=ch[i+1:i+d+1]
                  ch2=ch3[::-1]
                  i=i+d+1-ch2.index('1')-1
                  com+=1
            else:
                  print(-1)
                  break
