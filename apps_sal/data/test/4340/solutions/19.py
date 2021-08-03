n = int(input())
v = list(map(int, input().split()))
for i in v:
    print(i - (i % 2 == 0), end=' ')
