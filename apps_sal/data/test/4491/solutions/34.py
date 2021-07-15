n = int(input())

lis = []
for _ in range(2):
    lis.append(list(map(lambda x: int(x), input().split(" "))))
max = 0
for i in range(n):
    su = sum(lis[0][:i + 1])
    su += sum(lis[1][i:])
    if su >= max:
        max = su

print(max)
