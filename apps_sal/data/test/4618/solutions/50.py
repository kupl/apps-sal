s = input()
K = int(input())

sub = set()
for i in range(K):
    for j in range(len(s) - i):
        sub.add(s[j:j + i + 1])

sub = list(sub)
sub.sort()

print(sub[K - 1])
