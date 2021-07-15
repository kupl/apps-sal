n = int(input())
data = list(map(int,input().split()))

d = set()

for el in data:
    d.add(el)

for el in d:
    if el % 2 == 0:
        for  i in range(n):
            if data[i] == el:
                data[i] -= 1


print(" ".join(str(el) for el in data))

