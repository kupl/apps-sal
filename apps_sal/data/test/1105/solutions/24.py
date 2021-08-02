recovery = [-1] * 100001
solution = int(input())
for s in range(solution):
    sol, user = map(int, input().split())
    # Consecutive numbers should be 1 apart
    if recovery[user] == sol - 1:
        recovery[user] = sol
    # Skip duplicates
    elif recovery[user] >= sol:
        continue
    else:
        # exit out of the program
        print('NO'); return
print('YES')
