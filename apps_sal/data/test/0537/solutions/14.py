numList = input().split(" ")
n = int(numList[0])
k = int(numList[1])
d = (n // 2) // (k + 1)
c = k * d
other = n - c - d
print(d, c, other)
