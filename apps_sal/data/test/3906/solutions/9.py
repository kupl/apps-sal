def task_1(n, m): # n - строки m - столбцы
    counts = 8
    last = 0
    current = 1
    fn = fm = None
    for i in range(0, max(n, m)+1):
        if n == i:
            fn = current
        if m == i:
            fm = current
        last, current = current, last + current
        
    counts = 2*(fn + fm - 1)
    print(counts%(10**9+7))

def __starting_point():
    # Number of requests
    n, m = (map(int, input().rstrip().split()))
    task_1(n, m)
__starting_point()
