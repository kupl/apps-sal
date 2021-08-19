n = int(input())
a = list(map(int, input().split()))
exist_odd = False
in_for = 0
while exist_odd == False:
    for i in range(n):
        if a[i] % 2 != 0:
            exist_odd = True
            if n != i:
                in_for -= 1
            break
        else:
            a[i] = a[i] / 2
    in_for += 1
print(in_for)
