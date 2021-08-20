(N, K) = map(int, input().split())
Alist = list(map(int, input().split()))
already = [1]
alreadyset = {1}
last = 1
while True:
    if Alist[last - 1] in alreadyset:
        start = already.index(Alist[last - 1])
        break
    already.append(Alist[last - 1])
    alreadyset.add(Alist[last - 1])
    last = Alist[last - 1]
roop = len(already) - start
if K - len(already) < 0:
    print(already[K])
else:
    index = (K - start) % roop + start
    while not start <= index < len(already):
        index = index % roop + start
    print(already[index])
