s = int(input())
a = s
ans = 0

if (a == 1) or (a == 2) or (a == 4):
    ans = 4

else:

    for i in range(10**6 + 1):
        if a % 2 == 0:
            a = int(a / 2)
        else:
            a = 3 * a + 1

        if a == 4:
            ans = i + 5
            break

print(ans)
