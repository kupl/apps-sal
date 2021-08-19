(a, b) = map(int, input().split())


def F(a: int):
    if a % 2 == 1:
        if a % 4 == 1:
            return 1
        else:
            return 0
    else:
        return F(a + 1) ^ a + 1


ans = F(a - 1) ^ F(b)
print(ans)
