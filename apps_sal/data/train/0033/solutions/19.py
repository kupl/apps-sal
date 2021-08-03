for _ in range(int(input())):
    n = int(input())
    print(2, flush=False)
    print(f'{n} {n-1}', flush=False)
    if n > 2:
        print('\n'.join(f'{x} {x-2}' for x in range(n, 2, -1)))
