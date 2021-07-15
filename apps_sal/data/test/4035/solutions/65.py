A,B=map(int,input().split());a=0--A*25//2;c=B*10;print([int(max(a,c)),-1][(c+10<=a)|((A+1)*25//2<=c)])
