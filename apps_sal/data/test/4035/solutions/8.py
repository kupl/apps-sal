A,B=map(int,input().split());p=0.08;q=0.1;a=0--A//p;b=(A+1)//p;c=0--B//q;d=(B+1)//q;print([int(max(a,c)),-1][(d<=a)|(b<=c)])
