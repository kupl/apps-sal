n, m = map(int, input().split())
words = dict()
for i in range(m):
    w1, w2 = map(str, input().split())
    w = w1
    if len(w2) < len(w1):
        w = w2
    words[w1] = w
    words[w2] = w
data = input().split()
for i in range(n):
    print(words[data[i]], end=" ")
