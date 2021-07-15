n = int(input())
l = []
inline = input().split()
for i in range (n):
    l.append(int(inline[i]))
l.sort()
right_equal = 1
ans = 0
if len(l) >= 4:
    for i in range(len(l) - 2, -1, -1):
        if l[i] != l[i + 1]:
            if right_equal % 2 != 0:
                if l[i + 1] - l[i] == 1:
                    l[i + 1] -= 1
                    right_equal = 2
                else:
                    l.pop(i + 1)
            else:
                right_equal = 1
        else:
            right_equal += 1
if len(l) >= 4:
    if l[0] != l[1]:
        l.pop(0)
    flag = 1
    for i in range(len(l) - 2, -1, -2):
        if flag == 1:
            c = l[i]
        else:
            ans += c * l[i]
            c = 0
        flag = 1 - flag
print (ans)
