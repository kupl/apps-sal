N = int(input())
ans = ['-1']
for i in range(1, 41):
    for j in range(1, 31):
        n = 3 ** i + 5 ** j
        if n == N:
            ans = [str(i), str(j)]
            break
print(' '.join(ans))
