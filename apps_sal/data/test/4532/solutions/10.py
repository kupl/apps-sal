for test_i in range(int(input())):
    (n, k) = map(int, input().split())
    arr = list(map(lambda el: (k - int(el) % k) % k, input().split()))
    rems = {}
    for el in arr:
        if el:
            if el in rems:
                rems[el] += 1
            else:
                rems[el] = 1
    if rems:
        max_rem_item = max([(item[1], item[0]) for item in rems.items()])
        print(k * (max_rem_item[0] - 1) + max_rem_item[1] + 1)
    else:
        print(0)
