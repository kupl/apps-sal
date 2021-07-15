n = int(input())
data =[0]* 1000000
data[0] = n
i = 2
if n % 2 == 0:
    data[1] = n //2
else:
    data[1] = 3 * n + 1
while data[i - 1] not in data[0: i -2]:
    if data[i-1] % 2 == 0:
            data[i] = data[i - 1]//2
    else:
            data[i] = 3 * data[i - 1] + 1
    i += 1
print(i)
