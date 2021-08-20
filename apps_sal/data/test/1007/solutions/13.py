(k, p) = list(map(int, input().split()))
s = 0
for i in range(1, k + 1):
    s = (s + int(str(i) + str(i)[::-1])) % p
print(s)
