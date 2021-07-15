def func(v):
    n = len(v)
    for i in range(n):
        if v[v[v[i]]] == i:
            return True
    return False
def __starting_point():
    n = int(input())
    v = list(map(int, input().split()))
    for i in range(len(v)):
        v[i] -= 1
    if func(v):
        print("YES")
    else:
        print("NO")
__starting_point()
