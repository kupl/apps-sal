(apartments_nr, neighbours_nr) = (int(x) for x in input().split())
min_ans = int(apartments_nr != neighbours_nr)
if neighbours_nr == 0:
    min_ans = 0
max_ans = min(2 * neighbours_nr, apartments_nr - neighbours_nr)
print(min_ans, max_ans)
