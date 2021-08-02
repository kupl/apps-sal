n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))

# 0 to m-1 remainders
remainder = [0] * m
limit = n // m
moves = 0

for i in nums:
    remainder[i % m] += 1

for i in range(m):
    remainder[i] -= limit

deficit = set()
for i in range(m):
    if remainder[i] < 0:
        deficit.add(i)

# print(remainder)
# print(deficit)
spare = []
convert = {}

i = 0
while len(deficit) > 0:
    i = i % m

    if remainder[i] > 0:
        spare.append([i, remainder[i]])
        remainder[i] = 0
    elif remainder[i] < 0:
        if len(spare) > 0:
            while len(spare) > 0 and remainder[i] < 0:
                rem = min(spare[-1][1], abs(remainder[i]))

                if spare[-1][0] in list(convert.keys()):
                    convert[spare[-1][0]].append([(i - spare[-1][0]) % m, rem])
                else:
                    convert[spare[-1][0]] = [[(i - spare[-1][0]) % m, rem]]

                spare[-1][1] -= rem
                remainder[i] += rem

                if spare[-1][1] == 0:
                    spare.pop()

            if remainder[i] == 0:
                deficit.remove(i)

    i += 1

for i in range(n):
    rem = nums[i] % m

    if rem in list(convert.keys()):
        moves += convert[rem][-1][0]
        nums[i] += convert[rem][-1][0]
        convert[rem][-1][1] -= 1

        if convert[rem][-1][1] == 0:
            convert[rem].pop()

        if len(convert[rem]) == 0:
            del convert[rem]
# print(convert)
print(moves)
print(*nums)
