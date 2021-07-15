n = list(input())
n1 = list(input())

i = 0
cou = 0
while i != len(n):
    if n[i] != n1[i]:
        cou += 1
    i += 1

print(cou)
