c=0
D=1
for b,a in sorted([tuple(map(int,input().split()))[::-1] for _ in range(int(input()))]):
 c+=a
 if b<c:D=0

print('Yes' if D else 'No')
