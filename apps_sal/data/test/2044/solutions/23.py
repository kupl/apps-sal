(n, m) = list(map(int, input().split()))
data = list(map(int, input().split()))
answer = [0 for i in range(n)]
ind = 0
prev = 0
for el in data:
    val = prev + el
    t = val // m
    prev = val % m
    answer[ind] = t
    ind += 1
print(' '.join((str(el) for el in answer)))
