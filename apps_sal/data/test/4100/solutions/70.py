people,point,quiz = list(map(int,input().split()))
an = [int(input()) for _ in range(quiz)]
each_p = [point-quiz] * people

for x in an:
    each_p[x-1] += 1

for y in each_p:
    if y <= 0:
        print("No")
    else:
        print("Yes")

