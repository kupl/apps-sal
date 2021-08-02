N = int(input())
li = input().split('0')
for i in range(len(li)):
    li[i] = li[i].count('1')

if len(li) == 0:
    print("0")
else:
    li = list(map(str, li))
    print("".join(li))
