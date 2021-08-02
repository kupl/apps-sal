n, m, x, y = list(map(int, input().split()))
xl = list(map(int, input().split())) + [x]
yl = list(map(int, input().split())) + [y]
if max(xl) + 1 <= min(yl):
    print("No War")
else:
    print("War")
