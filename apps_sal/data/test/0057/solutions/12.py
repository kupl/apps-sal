n = int(input())
lst = []
for i in range(n):
    a, b = list(map(int, input().split()))
    lst.append([a, b])
if n == 1:
    print(-1)
elif n == 2 and lst[0][0] != lst[1][0] and lst[0][1] != lst[1][1]:
    print(abs(lst[0][0] - lst[1][0]) * abs(lst[0][1] - lst[1][1]))
elif n == 2:
    print(-1)

elif n == 3 or n == 4:
    if lst[0][0] != lst[1][0] and lst[0][1] != lst[1][1]:
        print(abs(lst[0][0] - lst[1][0]) * abs(lst[0][1] - lst[1][1]))
    elif lst[1][0] != lst[2][0] and lst[1][1] != lst[2][1]:
        print(abs(lst[1][0] - lst[2][0]) * abs(lst[1][1] - lst[2][1]))
    else:
        print(abs(lst[0][0] - lst[2][0]) * abs(lst[0][1] - lst[2][1]))
