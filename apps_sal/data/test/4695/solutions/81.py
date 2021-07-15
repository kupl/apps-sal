group = [0,2,0,1,0,1,0,0,1,0,1,0]
x,y = map(int, open(0).readline().split())
print('Yes' if group[x-1] == group[y-1] else 'No')
