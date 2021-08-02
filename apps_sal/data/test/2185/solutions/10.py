t = int(input())

for case in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    deltas = [0]
    delta_types = set([0])
    for i in range(len(arr2)):
        delta = arr2[i] - arr1[i]
        deltas.append(delta)
        delta_types.add(delta)
    if len(delta_types) > 2:
        print("NO")
    elif len(delta_types) == 1:
        print("YES")
    else:
        min_delta = min(delta_types)
        if min_delta < 0:
            print("NO")
        else:
            num_change = 0
            for i in range(len(deltas) - 1):
                if deltas[i] == 0 and deltas[i + 1] != 0:
                    num_change += 1
            if num_change == 1:
                print("YES")
            else:
                print("NO")
