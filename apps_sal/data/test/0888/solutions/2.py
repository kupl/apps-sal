n = int(input())
p = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]

list = []

for i in range(n):
    list.append(s.index(p[i]) - i)

cost = 0
output = []

while list != [0] * n:
    for i in range(n):
        if list[i] != 0:
            increment = 1
            if list[i] < 0:
                increment = -1
            for j in range(i + increment, i + list[i] + increment, increment):
                if list[j] <= i - j:
                    output.append([i + 1, j + 1])
                    change = abs(i - j)
                    cost += change
                    temp = list[i] - change * increment
                    list[i] = list[j] + change * increment
                    list[j] = temp
                    break
print(cost)
print(len(output))
for i in output:
    print(i[0], i[1])
