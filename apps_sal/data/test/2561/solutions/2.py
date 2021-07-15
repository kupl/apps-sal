def solve():
    a = int(input())
    print(2**(bin(a)[2:].count('1')))
    
for _ in range(int(input())):
    solve()
