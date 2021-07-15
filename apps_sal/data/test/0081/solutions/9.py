a, b = input().split()
a, b = int(a), int(b)
a, b = min(a, b), max(a, b)

def eu(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return eu(a%b, b)
    return eu(a, b%a)

opt = b - a
factor = []
i = 1
while i**2 < opt+1:
    if opt % i == 0:
        factor.append(i)
        factor.append(int(opt/i))
    i+=1

target = a * b / eu(a, b)
drop = 0

for i in factor:
    firstupd = a - (a % i) + i
    secondupd = b - (b % i) + i
    dres = firstupd * int(secondupd/eu(firstupd,secondupd))
    if dres <= target:
        if dres == target:
            drop = min(i-(a%i),drop)
        else:
            target = dres
            drop = i-(a%i)
print(drop)
