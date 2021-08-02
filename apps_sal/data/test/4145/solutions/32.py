x = int(input())
ans = 0
if x == 2:
    ans = 2
elif x == 3:
    ans = 3
else:
    for i in range(x, 100004):
        check = True
        root = int(i ** 0.5) + 1
        for j in range(2, root):
            if i % j == 0:
                check = False
                break
            else:
                continue
        if check:
            ans = i
            break
print(ans)
