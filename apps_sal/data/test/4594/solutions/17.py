N = int(input())
D = [int(input()) for _ in range(N)]
D.sort()
count = 1
for i in range(1, len(D)):
    if D[i] != D[i - 1]:
        count += 1
print(count)
