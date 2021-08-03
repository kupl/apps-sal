import sys


#sys.stdin = open("input.txt")
#sys.stdout = open("output.txt", "w")

n = int(input())

di = [1]
i = 2
while n > 1:
    if i * i > n:
        break
    if n % i == 0:
        di += [i]
        while n % i == 0 and n > 1:
            n //= i
    i += 1

if n != 1:
    di += [n]

ans = 1
for item in di:
    ans *= item
print(ans)
