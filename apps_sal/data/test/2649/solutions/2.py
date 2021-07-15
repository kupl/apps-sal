def mdmax(x):
    a = []
    b = []
    for i in range(len(x)):
        a.append(x[i][0] - x[i][1])
        b.append(x[i][0] + x[i][1])
    return max(max(a) - min(a), max(b) - min(b))

n = int(input())
data = []
for i in range(n):
    ininput_data = input()
    input_data = list(map(int, ininput_data.split()))
    data.append(input_data)
print(mdmax(data))
