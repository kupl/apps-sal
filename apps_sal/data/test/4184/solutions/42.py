N = int(input())
w = list(map(int, input().split()))

wlist = []
for t in range(0, N - 1, 1):
    s1 = sum(w[:t + 1])
    s2 = sum(w[t + 1:])
    wlist.append(abs(s1 - s2))

answer = min(wlist)
print(answer)
