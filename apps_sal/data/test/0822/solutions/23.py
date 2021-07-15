n, m, z = list(map(int, str.split(input())))
print(len(set(range(n, z + 1, n)) & set(range(m, z + 1, m))))

