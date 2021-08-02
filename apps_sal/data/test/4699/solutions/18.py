def testa(n, d):
    for i in d:
        if str(i) in str(n):
            return 0
    return 1


n, k = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]

while not testa(n, d):
    n += 1
print(n)
