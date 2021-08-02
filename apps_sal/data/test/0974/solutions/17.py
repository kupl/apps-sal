'''input
3
add 1
remove
add 2
add 3
remove
remove
'''
n = int(input())
c = 1
l = []
t = 0
for _ in range(2 * n):
    i = input().split()
    if i[0] == "add":
        l.append(int(i[1]))
    else:
        if l:
            if l[-1] == c:
                l.pop()
            else:
                t += 1
                l = []
        c += 1
print(t)
