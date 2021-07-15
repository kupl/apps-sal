import math

n, a, b = list(map(int, input().strip().split()))
min_sq = n * 6

if a * b >= min_sq:
    print('{}\n{} {}'.format(a * b, a, b))
else:
    max_sq = math.inf

    swap = False
    if a > b:
        a, b = b, a
        swap = True

    a_n, b_n = a, b


    for i in range(a, int(math.ceil(math.sqrt(min_sq))) + 1):
        n_b = int(math.ceil(min_sq / i))

        if n_b < b:
            continue

        new_sq = n_b * i
        if new_sq < max_sq:
            max_sq = new_sq
            a_n = i
            b_n = n_b
    
    if swap:
        a_n, b_n = b_n, a_n
    print('{}\n{} {}'.format(max_sq, a_n, b_n))

