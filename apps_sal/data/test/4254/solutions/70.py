def sheep_and_wolves():
    S, W = map(int, input().split())
    res = "safe"
    if W >= S:
        res = "unsafe"
    print(res)


sheep_and_wolves()
