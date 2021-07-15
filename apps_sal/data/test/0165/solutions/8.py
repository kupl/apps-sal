mas = list(map(int, input().split()))
mas.sort()
ans = 0
if mas[2] != mas[1]:
    ans += mas[2] - mas[1] - 1
    mas[1] = mas[2] - 1
if mas[0] != mas[1]:
    if mas[1] == mas[2]:
        ans += mas[1] - mas[0] - 1
    else:
        ans += mas[1] - mas[0]
    mas[0] = mas[1]
print(ans)
