t = map(int, input().strip())
s = map(int, input().strip())

digits1 = [0] * 10  # makes a list of size 10 filled with zeros.
digits2 = [0] * 10

for i in t:
    digits1[i] += 1
digits1[2] += digits1[5]
digits1[6] += digits1[9]
digits1[5] = digits1[9] = 0

for i in s:
    digits2[i] += 1
digits2[2] += digits2[5]
digits2[6] += digits2[9]
digits2[5] = digits2[9] = 0

print(min(map(lambda x: digits2[x] // digits1[x] if digits1[x] != 0 else 999999, range(10))))
