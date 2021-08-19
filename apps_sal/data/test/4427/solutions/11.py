(r, D, x) = map(int, input().split())


def function(y):
    y = r * y - D
    return y


z = 1
while z <= 10:
    z += 1
    ans = function(x)
    x = function(x)
    print(ans)
