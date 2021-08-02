from collections import Counter

N, P = list(map(int, input().split()))
Ss = input()

if P == 2 or P == 5:
    ans = 0
    for i, S in enumerate(Ss):
        if int(S) % P == 0:
            ans += i + 1
else:
    As = [0]
    A = 0
    D = 1
    for S in Ss[::-1]:
        S = int(S)
        A = (A + S * D) % P
        As.append(A)
        D = D * 10 % P

    cnt = Counter()
    ans = 0
    for A in As:
        ans += cnt[A]
        cnt[A] += 1

print(ans)
