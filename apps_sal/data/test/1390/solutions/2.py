def __starting_point():
    inp = input()
    arr = inp.split(" ")
    n = int(arr[0])
    m = int(arr[1])
    inp = input()
    arr = inp.split(" ")
    L = []
    for s in arr:
        L.append(int(s))
    L.sort()
    diff = L[n-1]-L[0]
    for i in range(m-n+1):
        diff = min(diff,L[i+n-1]-L[i])
    print(diff)

__starting_point()
