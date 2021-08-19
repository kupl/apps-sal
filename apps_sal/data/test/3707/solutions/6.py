def main():
    (n, t, k, d) = list(map(int, input().split()))
    method_a = (n + k - 1) // k * t
    done = 0
    i = 0
    a_progress = b_progress = 0
    while done < n:
        a_progress += 1
        if a_progress == t:
            a_progress = 0
            done += k
        if d > 0:
            d -= 1
        else:
            b_progress += 1
            if b_progress == t:
                b_progress = 0
                done += k
        i += 1
    print('YES' if i < method_a else 'NO')


try:
    while True:
        main()
except EOFError:
    pass
