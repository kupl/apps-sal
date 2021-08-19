def won(l):
    l = list(l)
    return l.index(max(l))


def readline():
    return (int(i) for i in input().split())


(n, m) = readline()
first_winners = (won(readline()) for i in range(m))
a = [0] * n
for i in first_winners:
    a[i] += 1
print(won(a) + 1)
