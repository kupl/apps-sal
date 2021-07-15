n = int(input())
a = list(map(int, input().split()))
q = a.pop(0)
a.sort()
sum = 0
while q <= a[-1]:
    a[-1] -= 1
    a.sort()
    q += 1
    sum += 1
print(sum)


    

