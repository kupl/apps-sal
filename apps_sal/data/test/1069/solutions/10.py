N = int(input())
res = 1
if N % 4 == 0:
    res += 1 + 1 + 1
elif N % 3 == 0:
    res += 3 + 2 + 4
elif N % 2 == 0:
    res += 4 + 4 + 1
else:
    res += 2 + 3 + 4
print(res % 5)
