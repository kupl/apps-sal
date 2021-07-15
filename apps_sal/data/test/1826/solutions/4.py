n=int(input())
S=input()

index = 0
summ=0

while index+1 < n:

    if S[index]!=S[index+1]:
        summ+=1
        index+=1

    index +=1

print(n-summ)

