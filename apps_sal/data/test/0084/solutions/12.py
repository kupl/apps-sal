n = int(input())
if n <= 4:
    print(n * (n - 1) // 2)
    return
a = 9
while int(str(a) + '9') <= 2 * n - 1:
    a = int(str(a) + '9')
ans = 0
for i in range(0, 9):
    r = int(str(i) + str(a))
    if r > 2 * n - 1:
        break
    ku = r - n
    if ku < 1:
        ans += r // 2
    elif ku < n:
        ans += (n - ku + 1) // 2
print(ans)
