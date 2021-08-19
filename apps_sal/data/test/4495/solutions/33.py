def LI():
    return list(map(int, input().split()))


(a, b, x) = LI()
ans = b // x - (a - 1) // x
print(ans)
