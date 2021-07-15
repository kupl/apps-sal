N = int(input())
count = 0
for i in range(1,N+1):
    M = N//i
    count += i*(M*(M+1)//2)
print(count)
