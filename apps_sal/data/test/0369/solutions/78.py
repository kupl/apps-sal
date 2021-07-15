N, M = list(map(int, input().split()))
S = input()

lst = []
i = N
while i > 0:
    for j in range(min(i, M), 0, -1):
        if S[i - j] == '0':
            lst.append(j)
            i -= j
            break
    else:
        print((-1))
        return
print((' '.join(map(str, reversed(lst)))))

