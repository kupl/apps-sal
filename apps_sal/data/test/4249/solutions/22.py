_ = input()
n, m = _.split()
n, m = int(n), int(m)
_ = input()
_a = _.split()
b = []
num_list = []
_counter = {}
_sum = 0
for i in _a:
    value = int(i)
    _sum = _sum + value
    b.append(value)
    if value in _counter:
        _counter[value] = _counter[value] + 1
    else:
        _counter[value] = 1
        num_list.append(value)
if m > _sum:
    print("-1")
else:
    num_list.sort()
    num_list.reverse()
    counter = []
    sum_list = []
    whole_sum_list = []
    _ = 0
    __ = 0
    for num in num_list:
        num_count = _counter[num]
        counter.append(num_count)
        _ = _ + num_count
        __ = __ + num_count * num
        sum_list.append(_)
        whole_sum_list.append(__)

    def avail(k):
        parse = len(num_list) - 1
        for i in range(len(num_list)):
            if sum_list[i] // k >= num_list[i]:
                parse = i
                break
        parse = parse - 1 if parse > 0 else 0
        floor = sum_list[parse] // k - 1
        token = sum_list[parse] % k
        # print(k, sum_list[parse], floor, token)
        whole_sum = whole_sum_list[parse] - k * int(floor * (floor + 1) // 2) - token * (floor + 1)
        if whole_sum >= m:
            return True
        if len(num_list) == 1:
            return False
        floor = floor + 1
        _value = num_list[parse + 1]
        for i in range(counter[parse + 1]):
            if _value <= floor:
                break
            if whole_sum >= m:
                return True
            whole_sum = whole_sum + _value - floor
            # print(k, i, whole_sum)
            token = token + 1
            if token >= k:
                floor, token = floor + 1, 0
        if whole_sum >= m:
            return True
        return False

    def _avail(k):
        token = 0
        floor = 0
        cafe = 0
        available = False
        for value, count in zip(num_list, counter):
            if cafe - floor * token >= m:
                available = True
            if floor >= value:
                break
            cafe = cafe + value * count
            token = token + count
            for i in range(0, token // k):
                cafe = cafe - (floor + i) * k
            floor = floor + token // k
            token = token % k
        if cafe - floor * token >= m:
            available = True
        return available

    start = 1
    end = n
    while start != end:
        k = (start + end) // 2
        # print(start,end,avail(k))
        if avail(k):
            start, end = start, k
        else:
            start, end = k + 1, end
    if n == 1:
        print(1)
    else:
        print(start)
