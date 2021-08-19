n = int(input())
s = 'I hate '
for i in range(1, n):
    if i % 2 == 1:
        s += 'that I love '
    else:
        s += 'that I hate '
s += 'it'
print(s)
