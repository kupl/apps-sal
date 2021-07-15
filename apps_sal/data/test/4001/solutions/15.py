input()

lst = list(map(int, input().split()))
lst.sort()
first = lst[-1]

i = 1
while i <= first:
    if first % i == 0:
        lst.remove(i)
    i += 1

print(first, lst[-1])

