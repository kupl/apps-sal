(a, b) = list(map(int, input().split()))
k = 0
for i in range(a, b + 1):
    if str(i) == ''.join(list(reversed(str(i)))):
        k += 1
print(k)
