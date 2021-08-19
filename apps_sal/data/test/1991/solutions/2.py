t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    wrongcount = 0
    for i in range(n):
        if i > 0 and a[i - 1] == i and (a[i] != i + 1) and (wrongcount == 1):
            wrongcount = 2
        if a[i] != i + 1 and wrongcount == 0:
            wrongcount = 1
    print(wrongcount)
