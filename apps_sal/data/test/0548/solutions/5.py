n = int(input())
l = list(map(int,input().split(' ')))

suma = sum(l)
b = False

for x in l:
    if x % 2 == 1:
        b = True

print(["Second","First"][b])

