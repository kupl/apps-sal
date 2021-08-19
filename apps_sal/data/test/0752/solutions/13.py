n = int(input())
num = []
for i in range(n):
    s = input()
    num.append(s)
num2 = []
for i in range(n):
    s = input()
    num2.append(s)
i = 0
ans = 0
while i < len(num):
    if num[i] in num2:
        num2.pop(num2.index(num[i]))
        num.pop(i)
    else:
        i += 1
while len(num):
    x = num[0]
    if True:
        best = -1
        min_el = 10000
        for i in range(len(num2)):
            if len(num2[i]) == len(x):
                ans += 1
                num2.pop(i)
                num.pop(0)
                break
print(ans)
