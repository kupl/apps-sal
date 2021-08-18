n = int(input())
a = sorted(zip(list(map(int, input().split())), list(range(n))), key=lambda x: (x[0], -x[1]), reverse=True)
m = int(input())
for i in range(m):
    k, pos = list(map(int, input().split()))
    b = sorted(a[:k], key=lambda x: x[1])
    print(b[pos - 1][0])
