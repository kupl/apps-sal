N, A, B = map(int, input().split())

sum = 0
for i in range(N+1):
    x = 0
    for j in range(len(str(i))):
        x = x + int(str(i)[j])
    if A <= x <= B:
        sum = sum + i
print(sum)
