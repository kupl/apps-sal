n = int(input())

r = [int(i) for i in input().split()]
mas=[]
for i in range(n):
    mas.append(sum(r[:i+1]))

k=0
for i in range(n):
    for j in range(i, n):
        if ((mas[j] - mas[i] + r[i]) > (100*(j-i+1))) and (j-i+1 > k):
            k = j-i+1
print(k)

