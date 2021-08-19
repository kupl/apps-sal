import random
N = int(input())
arr = list(map(int, input().split()))
uniq = set(arr)
uniq.remove(0)
not_found = [x for x in range(1, N + 1) if x not in uniq]
while True:
    random.shuffle(not_found)
    arr2 = arr.copy()
    idx = 0
    for i in range(N):
        if arr2[i] == 0:
            arr2[i] = not_found[idx]
            idx += 1
    if not any((i + 1 == x for (i, x) in enumerate(arr2))):
        print(' '.join(map(str, arr2)))
        break
