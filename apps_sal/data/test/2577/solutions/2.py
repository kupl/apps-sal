for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    for i in range(n):
        print(*(a + (a + i + j) % 2 for j, a in enumerate(map(int, input().split()))))
