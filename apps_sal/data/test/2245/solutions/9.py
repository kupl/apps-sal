T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    if k % 3:
        if n % 3:
            print("Alice")
        else:
            print("Bob")
    else:
        loop = k + 1
        idx = n % loop
        if idx == k:
            print("Alice")
        elif idx % 3:
            print("Alice")
        else:
            print("Bob")

    '''
    sg = [0] * (n+3)
    sg[1] = 1
    sg[2] = 1
    for i in range(3, n+1):
        if sg[i-1] == 0:
            sg[i] = 1
        elif sg[i-2] == 0:
            sg[i] = 1
        elif i >= k and sg[i-k] == 0:
            sg[i] = 1
        else:
            sg[i] = 0
    if sg[n]:
        print("Alice")
    else:
        print("Bob")
    print(sg)
    '''
