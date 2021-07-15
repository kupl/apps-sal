k=int(input())
rem=0

for i in range(k):
    rem=(10*rem+7)%k
    if rem==0:
        print(i+1)

        break
    if i==k-1:
        print(-1)
