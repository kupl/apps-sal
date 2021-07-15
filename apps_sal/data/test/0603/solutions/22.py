rgb = list(map(int, input().split()))

def bouquets(rgb, combined):
    combined = min(combined, min(rgb))
    return combined + sum((x - combined) // 3 for x in rgb)

print(max(bouquets(rgb, combined) for combined in range(3)))
