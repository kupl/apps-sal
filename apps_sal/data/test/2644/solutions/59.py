N = int(input())
P = list(map(int, input().split()))

bef = 1
ans = []
for i in range(N):
    # find bef
    if P[i] == bef:
        for j in range(i, bef - 1, -1):
            # Move bef to it's postion with serial swapping from i to bef-1
            P[j], P[j - 1] = P[j - 1], P[j]
            ans.append(j)
        # update bef to min updatable position owner
        bef = i + 1

if len(ans) != (N - 1) or P != sorted(P):
    # not using entire swap or unsorted without duplicate
    print('-1')
else:
    print('\n'.join(map(str, ans)))
