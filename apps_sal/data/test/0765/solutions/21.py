(t, s, q) = list(map(int, input().split()))
lecture = 0
sol = 1
pas = 1 - 1 / q
piste = s
while piste < t:
    x = q * (piste - lecture)
    if piste + x * pas < t:
        sol += 1
        piste += x * pas
        lecture = 0
    else:
        break
print(sol)
