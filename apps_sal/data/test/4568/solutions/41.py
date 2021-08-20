N = int(input())
S = input()


def check(i):
    return len(set(S[:i]) & set(S[i:]))


ans = [0] * N
for i in range(N):
    ans[i] = check(i)
print(max(ans))
