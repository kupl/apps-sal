N = int(input())
A = tuple(map(int, input().split()))
state = [0] * (N + 1)
for i in range(N, 0, -1):
    if N < i + i:
        state[i] = A[i - 1]
    else:
        state[i] = A[i - 1]
        j = i + i
        while j <= N:
            state[i] ^= state[j]
            j += i
ans = [str(i) for (i, x) in enumerate(state) if x == 1]
print(len(ans))
if ans:
    print(' '.join(ans))
