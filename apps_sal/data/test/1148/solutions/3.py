n = int(input())
numbers = input().split(" ")
mi = 10000000007
for i in range(len(numbers)):
    mi = min(mi, int(numbers[i]))
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])-mi

ret = 0
length = 0
j=0
while numbers[j] > 0:
    j+=1
for i in range(len(numbers)):
    if numbers[i] != 0:
        length+=1
    else:
        ret = max(ret, length)
        length = 0
ret = max(ret, length+j)
print(ret+n*mi)

