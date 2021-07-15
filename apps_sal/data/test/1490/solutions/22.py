string = input().split()
n = int(string[0])
m = int(string[1])
types = list(map(int, input().split()))
types = set(types)


curr = 1
res = []
while m > 0:
    if m - curr < 0:
        break
    if curr not in types:
        m -= curr
        res.append(str(curr))
    curr += 1

print(len(res))
print(' '.join(res))

