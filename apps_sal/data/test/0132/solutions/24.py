def solution(sectors):
    n = len(sectors)
    if n == 1:
        return sectors[0]
    else:
        min_diff = 360
        for i in range(n):
            j = i
            sum_sector = 0
            prev = sum_sector
            while sum_sector <= 180:
                prev = sum_sector
                sum_sector += sectors[j]
                j += 1
                j %= n
            if abs(360 - 2 * sum_sector) < min_diff:
                min_diff = abs(360 - 2 * sum_sector)
            if abs(360 - 2 * prev) < min_diff:
                min_diff = abs(360 - 2 * prev)
        return min_diff


n = int(input())
sectors = []
sectors_str = input().split()
for s in sectors_str:
    sectors.append(int(s))
print(solution(sectors))
