n = int(input())

a = list(map(int, input().split()))

count = 0
neg = 0
flag = False

for i in a:
    if i > 0:
        count += i - 1
    elif i < 0:
        count += - i - 1
        neg += 1
    else:
        count += 1
        flag = True

if not flag:
    if neg%2 == 1:
        count += 2

print(count)
