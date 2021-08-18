n = int(input())

if n == 1:
    print(1, 0)
    return

factors = {}
mindegree = float("inf")
maxdegree = 0
answer = 1

for x in range(2, int(n ** 0.5) + 1):
    if n == 1:
        break
    multiplicity = 0
    while n % x == 0:
        n = n // x
        multiplicity += 1
    if multiplicity:
        answer *= x
        #factors[x] = multiplicity
        mindegree = min(mindegree, multiplicity)
        maxdegree = max(maxdegree, multiplicity)

if n != 1:
    #factors[n] = 1
    answer *= n
    mindegree = min(mindegree, 1)
    maxdegree = max(maxdegree, 1)

deg = 0
while 2 ** deg < maxdegree:
    deg += 1

result = deg + 1
if 2 ** deg == maxdegree == mindegree:
    result -= 1
print(answer, result)
