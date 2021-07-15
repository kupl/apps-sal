A,B=map(int,input().split())
count=0
for i in range(A,B+1):
    if str(i)[0:2] == str(i)[::-1][:2]: count += 1
print(count)
