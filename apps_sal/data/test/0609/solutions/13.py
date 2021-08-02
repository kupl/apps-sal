def test(sq, n):
    a, b = sq[0][0], sq[0][1]
    if a == b:
        return False
    else:
        for i in range(n):
            if sq[i][i] != a or sq[i][-i - 1] != a:
                return False
        return sum([l.count(b) for l in sq]) == n * n - 2 * n + 1


n = int(input())
sq = []
for i in range(n):
    sq.append(input())

print("YES" if test(sq, n) else "NO")
