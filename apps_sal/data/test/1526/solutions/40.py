a,b,c=sorted(map(int,input().split()));d,e=c-a,c-b;print(d//2+e//2+(3-d%2-e%2)%3)
