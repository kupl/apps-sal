n = int(input())
j = 1
s = n
while j < n:
    s += (n - j) * j
    j += 1
print(str(s))
