# cook your dish here

def query(ar, k, a, b):
    return "Yes" if k <= a and k >= b else "No"


def __starting_point():
    n, t = map(int, input().split())
    ar = list(map(int, input().split()))
    large, small = max(ar), min(ar)
    for i in range(t):
        k = int(input())
        print(query(ar, k, large, small))


__starting_point()
