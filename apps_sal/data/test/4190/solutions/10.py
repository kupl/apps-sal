def solve(n, arr_a, arr_b):
    num_cnt = [0] * n
    for b in arr_b:
        num_cnt[b] += 1

    sol = []
    next_b = [i for i in range(1, n)] + [0]
    for a in arr_a:
        b = (n - a) % n 
        while num_cnt[b] == 0:
            if num_cnt[next_b[b]] == 0:
                next_b[b] = next_b[next_b[b]]
            b = next_b[b]

        num_cnt[b] -= 1
        sol.append((a+b) % n)
    return sol
            

def __starting_point():
    n = int(input().strip())

    arr_a = list(map(int, input().strip().split(" ")))
    arr_b = list(map(int, input().strip().split(" ")))

    sol = solve(n, arr_a, arr_b)

    print(" ".join(map(str, sol)))

__starting_point()
