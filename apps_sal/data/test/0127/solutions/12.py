def calc_income(cnt, customers):
    return min(cnt, max(0, customers - cnt))


n, f = map(int, input().split())

days = [tuple(map(int, input().split())) for i in range(n)]
days.sort(key=lambda elem: -calc_income(*elem))

ans = sum(map(lambda elem: min(elem[0], elem[1]), days))
for cnt, customers in days[:f]:
    ans += calc_income(cnt, customers)

print(ans)
