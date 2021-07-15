def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
N = int(input())
fac = factorization(N)
Answer = 0
for i in range(len(fac)):
    faci = fac[i][1]
    An = 1
    while faci >= An:
        Answer += 1
        faci -= An
        An +=1
if N == 1:
    Answer = 0
print(Answer)
