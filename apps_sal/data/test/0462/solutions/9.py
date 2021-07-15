a,b,c= map(int,input().split())
sr = (a+b+c - (min(a,b,c)+max(a,b,c)))
print(max(a,b,c) - sr + (sr - min(a,b,c)))
