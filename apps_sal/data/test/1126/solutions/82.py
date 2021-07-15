N, X, M = map(int, input().split())
A = X
loop = {A: 1}
sums = [0, A]
start = 0
end = 0
for i in range(2, M+2):
    A = (A ** 2) % M
    if A in loop:
        start = loop[A]
        end = i
        sums.append(sums[-1] + A)
        break
    sums.append(sums[-1] + A)
    loop[A] = i
answer = sums[start]
N -= start
answer += (N // (end - start)) * (sums[end] - sums[start])
answer += sums[start + N % (end - start)] - sums[start]
print(answer)
