N = int(input())
ls = []
for i in range(1, N + 1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    ls.append(i)
print(sum(ls))
