n = int(input())
a = list(map(int, input().split()))
q = int(input())

tmp = 0
l = [0 for i in range(10**5 + 1)]
for i in a:
    tmp += i
    l[i] += 1

for i in range(q):
    b, c = map(int, input().split())
    tmp += c * l[b] - b * l[b]
    print(tmp)
    l[c] += l[b]
    l[b] = 0
