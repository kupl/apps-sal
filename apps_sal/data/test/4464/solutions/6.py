a, b, c = map(int, input().split())
res = "NO"
for i in range(1, b + 1):  # bで割る=余りがb個の種類出る
    if (a * i) % b == c:
        res = "YES"
        break
print(res)
