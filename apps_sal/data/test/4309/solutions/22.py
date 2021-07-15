N = int(input())
lst = [i + i * 10 + i * 100 for i in range(1, 10)]

for l in lst:
    if N <= l:
        print(l)
        break
