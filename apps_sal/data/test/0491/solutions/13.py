n0 = str(input())
n1 = n0[:-1]
n2 = n0[:-2] + n0[-1:]
n0 = int(n0)
n1 = int(n1)
n2 = int(n2)
print(max(n1, n2, n0))
