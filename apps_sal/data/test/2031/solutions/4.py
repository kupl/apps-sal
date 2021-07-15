n = int(input())
data = input().split()
data1 = []
for i in range(n):
    data1.append((int(data[i]), i))
data1.sort(key=lambda x: (x[0], -x[1]))
for i in range(int(input())):
    k, pos = map(int, input().split())
    temp = sorted(data1[len(data1) - k:], key=lambda x: x[1])
    print(temp[pos - 1][0])
