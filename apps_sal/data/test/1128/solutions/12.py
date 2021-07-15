a,m = map(int,input().split())
while not m%2: m //= 2
print('No' if a%m else 'Yes')
