n = int(input())
a = input().split(' ')
for i in range(n):
    a[i] = int(a[i])
lu = {}
for i in range(n):
    lu[a[i]] = []
for i in range(n):
    lu[a[i]].append(i)
mins = []
maxes = []
for val in lu.values():
    mins.append(min(val))
    maxes.append(max(val))
key_num = len(lu.keys())
mins.sort()
maxes.sort()
ind = 0
pairs = 0
counter = key_num
for i in range(len(mins)):
    while maxes[ind] <= mins[i]:
        if ind == len(maxes) - 1:
            counter = 0
            break
        else:
            ind += 1
            counter -= 1
    pairs += counter
print(pairs)
