def case():
    n, k1, k2 = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if max(a) > max(b):
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    case()
