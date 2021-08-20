while 1:
    try:
        n = int(input())
        a = [int(item) for item in input().split()]
        for i in range(n):
            tour = a[i] // n
            if i < a[i] % n:
                tour += 1
            a[i] = tour
        min_tour = float('inf')
        for i in range(n):
            if a[i] < min_tour:
                answer = i
                min_tour = a[i]
        print(answer + 1)
    except EOFError:
        break
