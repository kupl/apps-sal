def main(r):
    n = int(input())
    lst = list(map(int, input().split()))
    win = 0
    i = 0
    while i < n and lst[i] == 1:
        i += 1
    if i % 2 == 0:
        if i == n:
            print("Second")
        else:
            print("First")
    else:
        if i == n:
            print("First")
        else:
            print("Second")






def __starting_point():
    t = int(input())
    for i in range(t):
        main(i)

__starting_point()
