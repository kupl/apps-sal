def check_fit_seal(grid, seal):
    if grid[0] >= seal[0] and grid[1] >= seal[1]:
        return True
    else:
        return False


def check_fit_seals(grid, seal1, seal2):
    ans = False
    if check_fit_seal(grid, seal1):
        ans = ans or check_fit_seal((grid[0] - seal1[0], grid[1]), seal2)
        ans = ans or check_fit_seal((grid[0], grid[1] - seal1[1]), seal2)
        ans = ans or check_fit_seal((grid[0] - seal1[0], grid[1]), (seal2[1], seal2[0]))
        ans = ans or check_fit_seal((grid[0], grid[1] - seal1[1]), (seal2[1], seal2[0]))

    seal1 = (seal1[1], seal1[0])
    if check_fit_seal(grid, seal1):
        ans = ans or check_fit_seal((grid[0] - seal1[0], grid[1]), seal2)
        ans = ans or check_fit_seal((grid[0], grid[1] - seal1[1]), seal2)
        ans = ans or check_fit_seal((grid[0] - seal1[0], grid[1]), (seal2[1], seal2[0]))
        ans = ans or check_fit_seal((grid[0], grid[1] - seal1[1]), (seal2[1], seal2[0]))

    return ans


n, a, b = [int(i) for i in input().strip().split(' ')]

seals = []
for _ in range(n):
    seals.append([int(i) for i in input().strip().split(' ')])

max_area = 0
for i, seal1 in enumerate(seals):
    for j, seal2 in enumerate(seals):
        if i != j:
            if check_fit_seals((a, b), seal1, seal2):
                max_area = max(max_area, seal1[0] * seal1[1] + seal2[0] * seal2[1])

print(max_area)

