N = int(input())
ans = 10**12
for i in range(1,int(N**0.5)+1):
    j = N/i
    if(j == int(j)):
        ans = i+j-2
print(int(ans))
