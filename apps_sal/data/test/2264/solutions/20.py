a = int(input())
Ans = []
for i in range(a):
    A = []
    x = int(input())
    B = []
    for j in range(x):
        (n, m) = list(map(int, input().split()))
        A.append(n)
        B.append(m)
    A.sort()
    B.sort()
    Ans.append(max(0, A[-1] - B[0]))
for b in Ans:
    print(b)
