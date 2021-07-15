n = int(input())
m = str(input())
j = 0
while j < n and m[j] == '1':
    j += 1
if j < n:
    print(j + 1)
else:
    print(n)


