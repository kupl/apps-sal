(A, B, X) = map(int, input().split())
D = min(10, X // B)
flag = 1
while X - B * D > 0:
    N = (X - B * D) // A
    if N >= 10 ** (D - 1):
        N = min(N, 10 ** D - 1)
        break
    if D < 1:
        flag = 0
        break
    D -= 1
if N > 10 ** 9:
    N = 10 ** 9
print(N if flag else flag)
