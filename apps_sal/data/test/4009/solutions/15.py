n,x,y = list(map(int,input().split()))
s = input()

print(s[-x:].count('1') - (1 if s[-y-1]=='1' else -1))
#print(s[-x:],s[-x:].count('1'),1 if s[-y-1]=='1' else 0)


