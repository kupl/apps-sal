n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

l.sort(key=lambda l:l[1])

t = 0

for i in l:
    t += i[0]
    if(t > i[1]):
        print("No")
        return
print("Yes")
