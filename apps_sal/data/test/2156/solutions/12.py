l = int(input())
numerals = list(map(int, input().split()))
requests_num = int(input())
requests = []
for i in range(requests_num):
    requests.append(list(map(int, input().split())))
numerals_combos = []
for i in range(l // 100):
    numerals_combos.append(sum(numerals[i * 100: (i + 1) * 100]))
for request in requests:
    l, r = request[0] - 1, request[1]
    if r - l >= 200:
        l_100 = l // 100 + 1
        r_100 = r // 100
        print(sum(numerals[l: l_100 * 100]) + sum(numerals_combos[l_100: r_100]) + sum(numerals[r_100 * 100: r]) // 10)
    else:
        print(sum(numerals[l: r]) // 10)
