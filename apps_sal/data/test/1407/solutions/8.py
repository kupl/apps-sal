def buil_prime_dict(n):
    lst = [0, 0] + [1] * n
    for i in range(2, n):
        if lst[i]:
            for j in range(i * i, n, i):
                lst[j] = 0
    for k in range(n, -1, -1):
        if lst[k]:
            ind = k
            lst[k] = 0
        else:
            lst[k] = ind - k
    return lst


prime_dict = buil_prime_dict(10 ** 5 + 100)
line1 = input()
n = int(line1.split(' ')[0])
m = int(line1.split(' ')[1])
matrix = []
max_num = 0
for j in range(n):
    line2 = input()
    d = [int(x) for x in line2.split(' ')]
    matrix.append(d)
matrix = [[prime_dict[y] for y in i] for i in matrix]
results = []
for x in matrix:
    results.append(sum(x))
for x in zip(*matrix):
    results.append(sum(x))
print(min(results))
