from math import *
n = int(input())
b = list(map(int, input().split(" ")))
maxim = max(b)
squad = []
for i in range(0, int(sqrt(maxim)) + 1):
    squad.append(i ** 2)

to_quad = 0
quad_list = []
not_quad = 0
not_quad_list = []
for i in range(0, len(b)):
    if sqrt(b[i]) == int(sqrt(b[i])):
        to_quad += 1
        quad_list.append(b[i])
    else:
        not_quad += 1
        not_quad_list.append(b[i])
if(to_quad == not_quad):
    print(0)
else:
    if(to_quad > not_quad):
        t = []
        answer = 0
        c = to_quad - int(n / 2)
        for i in range(0, len(quad_list)):
            if(quad_list[i] == 0):
                t.append(2)
            else:
                t.append(1)
        t = sorted(t)
        for i in range(0, c):
            answer += t[i]
        print(answer)
    else:
        c = not_quad - int(n / 2)
        t = []
        answer = 0
        for i in range(0, len(not_quad_list)):
            tmp = int(sqrt(not_quad_list[i]))
            r = (tmp + 1) ** 2
            l = (tmp - 1) ** 2
            t.append(min(abs(not_quad_list[i] - r), min(abs(not_quad_list[i] - tmp ** 2), abs(not_quad_list[i] - l))))
        t = sorted(t)
        for i in range(0, c):
            answer += t[i]
        print(answer)
