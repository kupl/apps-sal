n = int(input())
s = input()


def dif(x, a):
    num1 = ord(x) - ord('A')
    num2 = ord(a) - ord('A')
    return min(abs(num1 - num2), 26 - abs(num1 - num2))


A = []
for x in s:
    B = [dif(x, 'A'), dif(x, 'C'), dif(x, 'T'), dif(x, 'G')]
    A.append(B)
ans = 10 ** 10
for i in range(n - 3):
    m = A[i][0] + A[i + 1][1] + A[i + 2][2] + A[i + 3][3]
    if m < ans:
        ans = m
print(ans)
