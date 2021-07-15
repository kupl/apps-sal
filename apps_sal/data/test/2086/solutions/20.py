n = int(input())
ps = [ int(a) for a in input().split() ]
s,f = [ int(a) for a in input().split() ]

window = f-s
ps += ps[:window]

def f(x):
    return (s-1-x)%n + 1

answers = []
c = m = sum(ps[:window])
for i in range(n):
    if c > m:
        answers = [f(i)]
        m = c
    elif c == m:
        answers += [f(i)]
    c += ps[i+window]-ps[i]

print(min(answers))
