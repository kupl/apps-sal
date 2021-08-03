x = input()
arr = x.split(' ')
a = (int)(arr[0])
b = (int)(arr[1])
c = (int)(arr[2])

ans = set()

for i in range(1, 82):
    temp = b * (i**a) + c
    temp1 = 0
    temp2 = temp
    while temp > 0:
        temp1 = temp1 + (int)(temp % 10)
        temp = (int)(temp / 10)

    # print(temp2)
    # print(temp1)
    if temp2 > 0 and temp2 < 1000000000 and temp1 == i:
        ans.add(temp2)

print(len(ans))
answer = sorted(ans)

if len(ans) != 0:
    for i in answer:
        print(i, '', end='')
