n = int(input())
l = input().split()
li = [int(i) for i in l]
dp = [0 for i in range(n)]
if n == 1:
    print(li[0])
elif n == 2:
    print(li[0] | li[1])
else:
    maxa = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                curr = li[i] | li[j] | li[k]
                if curr > maxa:
                    maxa = curr
    print(maxa)
