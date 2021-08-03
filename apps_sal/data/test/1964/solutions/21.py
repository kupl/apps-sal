n = int(input())
peoples = [int(x) for x in input().split()]

sums = []
for i in range(n):
    sums.append(sum([int(x) * 5 for x in input().split()]) + 15 * peoples[i])

print(min(sums))
