def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    while True:
        min_num = min(a)
        a = list(map(lambda x: min_num if x % min_num == 0 else x % min_num, a))
        if all(i == min_num for i in a):
            print(min_num)
            break


resolve()
