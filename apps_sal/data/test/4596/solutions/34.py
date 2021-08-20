n = int(input())
a = list(map(int, input().split()))
count = 0
exist_odd = False
while exist_odd == False:
    for i in range(n):
        if a[i] % 2 != 0:
            exist_odd = True
            if n != i:
                count -= 1
            break
        else:
            a[i] = a[i] / 2
    count += 1
print(count)
