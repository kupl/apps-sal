n = int(input())
prices = [int(i) for i in input().split()]
people = []
for i in range(n):
    people.append([i + 1, prices[i]])
people.sort(key=lambda x: x[1])
print(str(people[-1][0]) + ' ' + str(people[-2][1]))
