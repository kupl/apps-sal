n = int(input())
f = [1, 1]
while f[-1] < n:
    f += [f[-1] + f[-2]]
if f[-1] == n:
    print(len(f) - 2)
else:
    print(len(f) - 3)
