def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


N = int(input())
A = list(map(int, input().split()))

Left = [A[0]]
for i in range(N - 1):
    Left.append(gcd(Left[i], A[i + 1]))

Right = [A[N - 1]]
for i in range(N - 1):
    Right.append(gcd(Right[i], A[N - 2 - i]))
Right.reverse()

ans_list = []
ans_list.append(Right[1])
for i in range(1, N - 1):
    ans_list.append(gcd(Left[i - 1], Right[i + 1]))
ans_list.append(Left[N - 2])

print(max(ans_list))
