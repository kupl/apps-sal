for k in range(int(input())):
    n = int(input())
    vec = list(map(int, input().split()))
    while vec[0] == 0:
        vec = vec[1:]
    while vec[-1] == 0:
        vec = vec[:-1]
    print(vec.count(0))
