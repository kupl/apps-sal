n = int(input())
ans = 0
temp = 3*10**5
n2 = temp *2 +1
ar = [0] * n2
while n > 0:
    si = input()
    numOp = 0
    numCl = 0
    num = 0
    num2 = 0
    last = 0
    for i in si:
        if i == "(":
            numOp += 1
        else:
            numCl += 1
            if numCl > numOp:
                num = max(num,numCl-numOp)
                last = numCl-numOp
    n-=1
    if numCl < numOp:
        num2 = numCl-numOp
    if num > last or (num > numCl-numOp and num != 0):
        continue
    if num2 == 0 and num >= 0:
        ar[temp+num] += 1
    else:
        ar[temp+num2] += 1
for i in range(temp+1):
    ans += ar[i] * ar[n2 - 1 - i]
print(ans)

