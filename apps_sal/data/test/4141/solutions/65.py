def solve():
    N = int(input())
    A = [int(i) for i in list(input().split())]
    for a in A:
        if a % 2 == 0:
            if not (a % 3 == 0 or a % 5 == 0):
                print('DENIED')
                return
    print("APPROVED")


solve()
