a, b, c = list(map(int, input().split()))
weeks = min(a//3, b//2, c//2)
a -= weeks * 3
b -= weeks * 2
c -= weeks * 2

days = ["f", "r", "c", "f", "c", "r", "f"]
ans = 0

for i in range(7):
    day = i
    anstemp = 0
    A = a
    B = b
    C = c
    for j in range(50):
        if days[day] == "f":
            if A > 0:
                A -= 1
                day += 1
                anstemp += 1
            else:
                break
        elif days[day] == "r":
            if B > 0:
                B -= 1
                day += 1
                anstemp += 1
            else:
                break
        else:
            if C > 0:
                C -= 1
                day += 1
                anstemp += 1
        if day == 7:
            day = 0
    ans = max(anstemp, ans)

ans += weeks * 7
print(ans)

