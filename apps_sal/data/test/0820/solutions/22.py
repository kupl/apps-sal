n = int(input())
m = int(input())
lst = []
rem = m
for i in range(n):
    tmp = int(input())
    lst.append(tmp)
lst.sort(reverse=True)
for (i, x) in enumerate(lst):
    rem -= x
    if rem <= 0:
        break
print(i + 1)
