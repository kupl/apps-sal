import itertools

n = int(input())
cubes = []
for i in range(n):
    line = input().split()
    cubes.append(line)

nums = {}
for i in range(1, 1000):
    nums[i] = False

if n == 3:
    for a in cubes[0]:
        for b in cubes[1]:
            for c in cubes[2]:
                for i in range(n):
                    for comb in itertools.permutations([a, b, c], i + 1):
                        pres = 0
                        for num in comb:
                            pres *= 10
                            pres += int(num)
                        nums[pres] = True


if n == 2:
    for a in cubes[0]:
        for b in cubes[1]:
            for i in range(n):
                for comb in itertools.permutations([a, b], i + 1):
                    pres = 0
                    for num in comb:
                        pres *= 10
                        pres += int(num)
                    nums[pres] = True

if n == 1:
    for a in cubes[0]:
        nums[int(a)] = True

x = 0
while(nums[x + 1]):
    x += 1
print(x)
