N = int(input())
basis = [(-2) ** d for d in range(64)]
cs = [1, -2]
for i in range(2, len(basis)):
    cs.append(cs[i - 2] + basis[i])
S = ['0'] * len(basis)
n = N
max_i = 0
while n != 0:
    if n > 0:
        for i in range(0, len(basis), 2):
            if cs[i] >= n:
                S[i] = '1'
                n -= basis[i]
                max_i = max(max_i, i)
                break
    else:
        for i in range(1, len(basis), 2):
            if cs[i] <= n:
                S[i] = '1'
                n -= basis[i]
                max_i = max(max_i, i)
                break
print(''.join(S[:max_i + 1])[::-1])
