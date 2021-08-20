inputs = [int(string) for string in input().split()]
n = inputs[0]
k = inputs[1]
count = int(n / k)
array = [int(string) for string in input().split()]
summ = int(0)
various = []
for i in range(int(0), int(k)):
    various.append(0)
for i in range(len(array)):
    if array[i] == 1:
        various[i % k] += 1
    else:
        various[i % k] -= 1
for i in range(int(0), int(k)):
    summ += (count - abs(various[i])) / 2
print(int(summ))
