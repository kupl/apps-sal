''' بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ '''
# codeforces1169A_live
def gi(): return list(map(int, input().strip().split()))


n, a, x, b, y = gi()
while a != x and b != y:
    a += 1
    if a > n:
        a = 1
    b -= 1
    if b <= 0:
        b = n
    if a == b:
        print("YES")
        return
print("NO")
