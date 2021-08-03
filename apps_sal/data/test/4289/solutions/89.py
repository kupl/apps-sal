N = int(input())
T, A = list(map(int, input().split()))
H = [int(_) for _ in input().split()]

answer = 0
for i in range(len(H)):
    H[i] = abs(T - (H[i] * 0.006) - A)
    if H[answer] > H[i]:
        answer = i
print((answer + 1))
