def buil_prime_dict(n):
    a = [x for x in range(n + 1)]
    a[1] = 0
    lst = []
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    return lst


prime_dict = buil_prime_dict(10 ** 5 + 100)


def diff_search_number_prime(a, dictionary):
    start_ind = 0
    stop_ind = len(dictionary) - 1
    if a == 1:
        return 1
    while stop_ind - start_ind != 1:
        middle_ind = (stop_ind - start_ind) // 2 + start_ind
        if a == dictionary[middle_ind] or a == dictionary[start_ind] or a == dictionary[stop_ind]:
            return 0
        elif a > dictionary[middle_ind]:
            start_ind = middle_ind
        else:
            stop_ind = middle_ind
    return abs(a - dictionary[stop_ind])


line1 = input()
n = int(line1.split(' ')[0])
m = int(line1.split(' ')[1])
matrix = []
max_num = 0
for j in range(n):
    line2 = input()
    d = [int(x) for x in line2.split(' ')]
    matrix.append(d)
    if max_num < max(d):
        max_num = max(d)
dict_dist = [0, 1]
for i in range(2, max_num + 1):
    dict_dist.append(diff_search_number_prime(i, prime_dict))
matrix = [[dict_dist[y] for y in i] for i in matrix]
results = []
for x in matrix:
    results.append(sum(x))
for x in zip(*matrix):
    results.append(sum(x))
print(min(results))
