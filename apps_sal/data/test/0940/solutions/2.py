def solve():
    a = [int(x) for x in input().split()]
    print(max(0,max(a)-(sum(a)-max(a)) + 1))
solve()
# for _ in range(int(input())):

