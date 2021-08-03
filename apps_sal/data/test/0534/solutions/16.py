a = input().split(" ")
a = [int(i) for i in a]
n = input()
n = [i for i in n]
while a[1]:
    k = []
    for i in range(0, a[0]):
        if n[i] == 'B':
            k.append(i)
    for i in k:
        if i < a[0] - 1 and n[i + 1] == 'G':
            n[i] = 'G'
            n[i + 1] = 'B'
    a[1] -= 1
print("".join(n))
