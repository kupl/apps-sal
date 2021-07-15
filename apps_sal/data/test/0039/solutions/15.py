ch=input()
while(ch==ch[::-1] and len(ch)>=1):
      ch=ch[:-1]
if(len(ch)==1):
      print(0)
else:
      print(len(ch))
      

