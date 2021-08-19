(n, m) = list(map(int, input().split()))
arr = list(map(int, input().split()))
t = list(map(int, input().split()))
taxi = list()
for i in range(len(arr)):
    if t[i] == 1:
        taxi.append(arr[i])
taxi2 = list()
kek = 1
for i in range(len(taxi) - 1):
    taxi2.append([kek, taxi[i] + (taxi[i + 1] - taxi[i]) // 2])
    kek = taxi[i] + (taxi[i + 1] - taxi[i]) // 2 + 1
taxi2.append([kek, arr[-1]])
taxi3 = [0] * m
j = 0
for i in range(len(arr)):
    if arr[i] > taxi2[j][1]:
        j += 1
    if t[i] != 1:
        taxi3[j] += 1
print(' '.join(map(str, taxi3)))
