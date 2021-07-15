b, max_fuel, f, k = map(int, input().split())

now_fuel = max_fuel
ans = 0

part_1 = f
part_2 = b - f

now_fuel -= part_1
if now_fuel < 0:
    print('-1')
    return

while k != 0:
    if k > 1:
        if now_fuel < part_2 * 2:
            ans += 1
            now_fuel = max_fuel
        now_fuel -= part_2 * 2
        k -= 1
        if now_fuel < 0:
            print('-1')
            return
    else:
        if now_fuel < part_2:
            ans += 1
            now_fuel = max_fuel
        now_fuel -= part_2
        k -= 1
        if now_fuel < 0:
            print('-1')
            return
        break

    if k > 1:
        if now_fuel < part_1 * 2:
            ans += 1
            now_fuel = max_fuel
        now_fuel -= part_1 * 2
        k -= 1
        if now_fuel < 0:
            print('-1')
            return
    else:
        if now_fuel < part_1:
            ans += 1
            now_fuel = max_fuel
        now_fuel -= part_1
        k -= 1
        if now_fuel < 0:
            print('-1')
            return
        break

print(ans)
