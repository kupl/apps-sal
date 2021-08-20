(n, q) = map(int, input().split())
s = input()
for _ in range(q):
    (l, r, c1, c2) = input().split()
    (l, r) = (int(l), int(r))
    s = [c2 if i + 1 >= l and i + 1 <= r and (s[i] == c1) else s[i] for i in range(len(s))]
print(''.join(s))
