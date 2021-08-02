s = str(input())

prev_sum = 0

ans = 0
f_el = 0
need = True
for el in s:
    el = int(el)

    if el % 3 == 0:
        ans += 1
        prev_sum = 0
        need = True
        continue

    if need:
        f_el = el
        need = False
        prev_sum = el
        continue

    prev_sum += el

    if prev_sum % 3 == 0 or (prev_sum - f_el) % 3 == 0:
        ans += 1
        prev_sum = 0
        need = True


print(ans)
