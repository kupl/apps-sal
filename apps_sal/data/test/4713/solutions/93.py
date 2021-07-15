n = int(input())
s = input()
max = 0
sum = 0
for i in s:
    if(i == 'I'):
        sum += 1
        if(max < sum):
            max = sum
    else:
        sum -= 1
print(max)
