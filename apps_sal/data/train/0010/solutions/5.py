t = int(input())
for test in range(t):
    n = int(input())
    l = list(map(int, input().rstrip().split()))
    i = 0
    arr = list()
    arr.append(str(l[0]))
    while i+1 < n:
        if i+1 == n-1 or (l[i] < l[i+1] and l[i+1] > l[i+2]) or (l[i] > l[i+1] and l[i+1] < l[i+2]):
            arr.append(str(l[i+1]))
        i += 1
    print(len(arr))
    print(" ".join(arr))
