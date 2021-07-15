def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    if arr[0] < arr[-1]:
        print('YES')
    else:
        print('NO')

def __starting_point():
    for _ in range(int(input())):
        solve()
__starting_point()
