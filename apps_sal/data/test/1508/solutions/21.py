N = int(input())
num = []
i = 0
IN = input().split()
while(i < N):
    num.append(int(IN[i]))
    i = i + 1
num.sort()
num[0], num[len(num) - 1] = num[len(num) - 1], num[0]
for i in num:
    print(i, end=' ')
