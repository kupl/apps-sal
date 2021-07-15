n = int(input())
odd = list()
even = list()

for i in range(n):
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odd.append(i)

print(len(odd) * len(even))
