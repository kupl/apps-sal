N = int(input())
li = []
for i in range(N):
    (a, b) = input().split()
    b = int(b)
    li.append([a, 100 - b, i + 1])
li.sort()
for j in range(N):
    print(li[j][2])
