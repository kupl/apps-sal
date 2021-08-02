n = int(input())
choco = [int(x) for x in input().split()]
m = int(input())
kup = [int(x) for x in input().split()]
choco.sort(reverse=True)
summa = sum(choco)
for item in kup:
    print(summa - choco[item - 1])
