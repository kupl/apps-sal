n = int(input())

li = [i for i in range(1,n+1) if i % 3 != 0 ]

sum = 0
for i in li:
    if i % 5 != 0:
        sum += i

print(sum)
