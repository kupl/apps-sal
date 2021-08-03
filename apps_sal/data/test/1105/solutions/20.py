c = [0] * 100001

for i in range(int(input())):

    x, k = list(map(int, input().split()))

    if x == c[k]:

        c[k] += 1

    elif x > c[k]:

        print('NO')

        return

print('YES')


# Made By Mostafa_Khaled
