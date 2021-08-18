import math

sa2 = input().split(' ')
candies = int(sa2[1])
sa22 = input().split(' ')
sa3 = [int(x) for x in sa22]

sa4 = []
for element in sa3:
    sa4.append(math.ceil(element / candies))
sa4.reverse()
print(int(sa2[0]) - sa4.index(max(sa4)))
