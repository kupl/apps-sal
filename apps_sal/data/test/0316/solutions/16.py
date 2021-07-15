n=int(input())
answer=0
for i in range(1,2*n-2,2):
    answer+=i
print(answer*2+2*n-1)

