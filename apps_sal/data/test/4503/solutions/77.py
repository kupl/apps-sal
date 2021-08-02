H, N = map(int, input().split())
A = list(map(int, input().split()))


def hissatu():
    HP = H - sum(A)
    if HP > 0:
        return "No"
    else:
        return "Yes"


print(hissatu())
