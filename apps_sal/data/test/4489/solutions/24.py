# B - Two Colors Card Game
N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]
s_set = list(set(s))

maxim = 0
for i in s_set:
    count = 0
    for j in s:
        if i == j:
            count += 1
    for k in t:
        if i == k:
            count -= 1
    if maxim < count:
        maxim = count
print(maxim)
