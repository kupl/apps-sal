Value = [int(input()) for _ in range(5)]
amari = list()
for i in range(5):
    if Value[i] % 10 == 0:
        amari.append(10)
    else:
        amari.append(Value[i] % 10)
min_amari = [i for i in range(5) if min(amari) == amari[i]]
ans = 0
for i in range(5):
    if i == min_amari[0]:
        ans += 0
    else:
        ans += Value[i] + 10 - amari[i]
ans += Value[min_amari[0]]
print(ans)
