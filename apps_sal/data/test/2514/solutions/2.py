n = int(input())
a = list(map(int, input().split()))
al = [0] * (10**5 + 1)
s = 0
for i in a:
    al[i] += 1
    s += i
q = int(input())
for _ in range(q):
    b, c = map(int, input().split())
    s = s + (c - b) * al[b]
    al[c] += al[b]
    al[b] = 0
    print(s)
