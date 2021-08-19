n = int(input())

k = list(map(int, input().split()))

#print('k: ', k)

m = []

for i in range(n):
    m.append(list(map(int, input().split())))

#print('m: ', m)

time = []

for i in range(len(k)):
    time.append(0)
    for j in range(len(m[i])):
        time[i] += m[i][j] * 5
        time[i] += 15

# print(time)
print(min(time))
