n = int(input())
a = input().split()
b = input().split()
ara = []
arb = []
for i in a:
    ara.append(int(i))
for i in b:
    arb.append(int(i))
ara.sort()
arb.sort()
i = 0
sumsa = 0
sumsb = 0
while i < n:
    if len(arb) == 0:
        sumsa += ara[-1]
        ara.pop()
    elif len(ara) == 0:
        arb.pop()
    elif arb[-1] > ara[-1]:
        arb.pop()
    else:
        sumsa += ara[-1]
        ara.pop()
    if len(ara) == 0:
        sumsb += arb[-1]
        arb.pop()
    elif len(arb) == 0:
        ara.pop()
    elif ara[-1] > arb[-1]:
        ara.pop()
    else:
        sumsb += arb[-1]
        arb.pop()
    i += 1
print(sumsa - sumsb)
