# 1  2  3  2  3  1  3
#  12 23 32 23 31 13
# 1 1 2 3 2 3 3 1 1 3
#      112 123 232 323 233 331 311 113
# 12/21  1   0   0   0   0   1   0   0
# 23/32  0   1   1   1   0   0   0   0
# 13/31  0   1   0   0   0   1   0   0


# 1 2 3 1 2 3 1 2 3| 1
# 	    123 231 312 123 231 312 123 231
# 12/21  1   1   1   0   1   1   0   1
# 23/32  1   1   0   1   0   1   1   0
# 13/31  1   1   0   1   1   0   1   1

# with open('h.in', 'r') as inputFile, open('h.out', 'w') as outputFile:
# (n,k) = [int(x) for x in inputFile.readline().strip().split(' ')]
# dataF = inputFile.readline().strip().split(' ');
(n, k) = [int(x) for x in input().strip().split(' ')]
dataF = input().strip().split(' ')
dataF = [int(x) for x in dataF]
data = [0]
for i in range(len(dataF)):
    if (data[len(data) - 1] != dataF[i]):
        data.append(dataF[i])
data = data[1:]
res = {x: 0 for x in set(data)}
res[data[0]] += 1
res[data[len(data) - 1]] += 1
for i in range(0, len(data) - 2, 1):
    prev = data[i]
    curr = data[i + 1]
    next = data[i + 2]
    if (prev == next):
        res[curr] += 2
    if (prev != next):
        res[curr] += 1
print(max(res, key=res.get))
