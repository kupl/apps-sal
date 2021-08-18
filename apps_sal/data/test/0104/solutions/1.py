
n = int(input())
l = list(map(int, input().split()))
s = sum(l)

s2 = 0
for i in range(len(l)):
    s2 += l[i]
    if s2 >= s / 2:
        print(i + 1)
        break
