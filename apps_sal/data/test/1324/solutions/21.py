calEach=input().split()
squares=list(input())
calTot=0
for i in squares:
    n=int(i)-1
    calTot+=int(calEach[n])
print(calTot)

