n = int(input())
num = [int(i) for i in input().split()]
ran = [2] * n
if n > 2:
    for i in range(2, n):
        if num[i] == num[i - 1] + num[i - 2]:
            ran[i] = ran[i - 1] + 1
        else:
            ran[i] = 2
    print(max(ran))
else:
    print(n)
