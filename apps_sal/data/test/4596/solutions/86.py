n = int(input())
l = list(map(int, input().split()))
result = 0
loop = 0
while True:
    if all(x % 2 == 0 for x in l):
        result += 1
        for data in range(len(l)):
            l[data] = l[data]//2
    else:
        print(result)
        return

