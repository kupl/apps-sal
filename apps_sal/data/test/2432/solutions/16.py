n = int(input())
n = list(bin(n)[2:])
n = (6 - len(n)) * ["0"] + n
n_t = n.copy()
n[1] = n_t[5]
n[2] = n_t[3]
n[3] = n_t[2]
n[4] = n_t[4]
n[5] = n_t[1]
print(int(''.join(n), 2))
