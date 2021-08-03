n, k = input().split()
n = int(n)
k = int(k)
dip = n // (2 * (k + 1))
cert = dip * k
total = dip + cert
print(str(dip) + " " + str(cert) + " " + str(n - total))
