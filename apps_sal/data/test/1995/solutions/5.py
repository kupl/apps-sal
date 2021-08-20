S = [c for c in input()]
Q = int(input())
for _ in range(Q):
    (l, r, s) = map(int, input().split())
    length = r - l + 1
    s %= length
    S = S[:l - 1] + S[r - s:r] + S[l - 1:r - s] + S[r:]
print(''.join(S))
