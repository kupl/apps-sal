minutes = [int(input()) for i in range(5)]
if max(m % 10 for m in minutes) != 0:
    ones_place_min = min(m % 10 for m in minutes if m % 10 != 0)
    for m in minutes:
        if m % 10 == ones_place_min:
            ones_place_min = m
            break
    minutes.remove(ones_place_min)
    minutes = [m if m % 10 == 0 else (m + 9) // 10 * 10 for m in minutes]
    minutes.append(ones_place_min)
print(sum(minutes))
