_, t, c = tuple(map(int, str.split(input())))
index = -1
count = 0
for i, ct in enumerate(map(int, str.split(input()))):

    if ct > t:

        index = i

    elif i - index >= c:

         count += 1

print(count)

