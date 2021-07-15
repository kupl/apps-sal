def kagami_mochi():
    n = int(input())
    d = []
    for _ in range(n):
        d.append(int(input()))
    d.sort()
    d_unique = list(set(d))
    print(len(d_unique))
def __starting_point():
    kagami_mochi()
__starting_point()
