n = int(input())
caa = input()
cab = input()
cba = input()
cbb = input()
mod = 10 ** 9 + 7
group1 = [('A', 'A', 'A', 'A'), ('A', 'A', 'A', 'B'), ('A', 'A', 'B', 'A'), ('A', 'A', 'B', 'B'), ('A', 'B', 'A', 'B'), ('A', 'B', 'B', 'B'), ('B', 'B', 'A', 'B'), ('B', 'B', 'B', 'B')]
group2 = [('A', 'B', 'A', 'A'), ('B', 'A', 'B', 'A'), ('B', 'A', 'B', 'B'), ('B', 'B', 'A', 'A')]
group3 = [('A', 'B', 'B', 'A'), ('B', 'A', 'A', 'A'), ('B', 'A', 'A', 'B'), ('B', 'B', 'B', 'A')]
if (caa, cab, cba, cbb) in group1:
    print(1)
elif (caa, cab, cba, cbb) in group2:
    ans = 1
    for i in range(n - 3):
        ans *= 2
        ans %= mod
    print(ans)
else:
    a1 = -1
    a2 = 1
    for i in range(n):
        a3 = a1 + a2
        a3 %= mod
        a1 = a2
        a2 = a3
    else:
        ans = a3
    print(ans)
