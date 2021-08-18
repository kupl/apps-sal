import sys


def solve(a, b, m, M, weights, last, solution):
    if (a - b > 10):
        return False
    if m == M:
        print("YES")
        print(*solution)
        return True
    for w in weights:
        if w != last and b + w > a:
            solution[m] = w
            if (solve(b + w, a, m + 1, M, weights, w, solution)):
                return True
    return False


sys.setrecursionlimit(1500)

w = input()
m = int(input())
weights = []
for i in range(1, 11):
    if w[i - 1] == '1':
        weights.append(i)
weights.sort(reverse=True)
solution = [0 for x in range(0, m)]

if not solve(0, 0, 0, m, weights, -1, solution):
    print("NO")
