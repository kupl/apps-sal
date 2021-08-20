(a, b) = map(int, input().split())
bis = [0] * 50
'\n- F(A,B) = F(0,B) ^ F(0,A-1)\n- 2m ^ 2m+1 = 1\n'


def F(a):
    if a % 2 == 0:
        x = (a - 1) // 2
        return x % 2 ^ a
    else:
        x = a // 2
        return x % 2


ans = F(b) ^ F(a - 1)
print(ans)
