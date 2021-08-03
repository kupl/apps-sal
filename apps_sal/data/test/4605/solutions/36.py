N, A, B = map(int, input().split())
count = 0
for i in range(1, N + 1):
    acc = 0
    for j in range(len(str(i))):
        acc += int(str(i)[j])
    if acc >= A and acc <= B:
        count += i
print(count)
