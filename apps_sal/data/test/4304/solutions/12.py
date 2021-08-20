def Gauss_sum(n):
    return n * (n + 1) // 2


(a, b) = map(int, input().split())
for i in range(999):
    if Gauss_sum(i + 1) - a == Gauss_sum(i + 2) - b:
        print(Gauss_sum(i + 1) - a)
        break
