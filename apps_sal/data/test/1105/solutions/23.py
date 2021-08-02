recovery = [-1] * 100001
solution = int(input())
for s in range(solution):
    sol, user = map(int, input().split())
    if recovery[user] == sol - 1:
        recovery[user] = sol
    elif recovery[user] >= sol:
        continue
    else:
        print('NO'); return
print('YES')
