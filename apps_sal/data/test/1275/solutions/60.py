N, K = list(map(int, input().split(' ')))

K = abs(K)

result = 0
for i in range(K + 2, 2 * N + 1):
    AB = i
    CD = AB - K
    AB -= max(0, (AB - (N + 1)) * 2)
    CD -= max(0, (CD - (N + 1)) * 2)
    result += (AB - 1) * (CD - 1)

print(result)
