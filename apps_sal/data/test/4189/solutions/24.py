n=int(input())
black=0
white=0
for i in range(n):
    s=input().split()
    if s[1]=='soft':
        black+=1
    else:
        white+=1
i=1
while i%2 and (black>i*i//2+1 or white>i*i//2) or i%2==0 and (black>i*i//2 or white>i*i//2):
    i+=1
j=i+0
i=1
while i%2 and (white>i*i//2+1 or black>i*i//2) or i%2==0 and (white>i*i//2 or black>i*i//2):
    i+=1
print(min(i,j))

