(N, A, B) = map(int, input().split())
cnt = 0
sum = 0
i = 0
for i in range(N + 1):
    j = 0
    tmpsum = 0
    l = list(str(i))
    for j in l:
        tmpsum += int(j)
    if tmpsum >= A and tmpsum <= B:
        sum += i
print(sum)
