n = int(input())

l = list(map(int, input().split()))

s = sum(l)

cs = 0
for i in range(len(l)):
    cs += l[i]
    if cs * 2 >= s:
        print(i + 1)
        break
