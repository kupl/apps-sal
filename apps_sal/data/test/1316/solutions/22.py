n, k = input().split()
n, k = int(n), int(k)

s = input() + ' '

d = {}
prev = '!'
cont = 0

for char in s:
    if (char != prev) or (cont >= k):
        if (cont >= k):
            if (prev in d):
                d[prev] += 1
            else:
                d[prev] = 1

        prev = char
        cont = 1
    else:
        cont += 1

print(max(list(d.values()) + [0]))
