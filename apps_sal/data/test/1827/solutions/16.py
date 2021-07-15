mvalues = 10 ** 5 + 1
n = int(input())
size = list(map(int, input().split()))
length = sum(size) // n
count = [0] * (mvalues)
for v in size:
    count[v] += 1
for i in range(mvalues):
    while count[i]:
        count[i] -= 1
        count[length - i] -= 1
        print(i, length - i)
