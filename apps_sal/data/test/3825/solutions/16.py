n = int(input())
ans = 0
for i in range(9):
    for j in range(49):

        def check(y, x):
            for i in range(49):
                for j in range(9):
                    if i == x and j == y:
                        continue
                    t = (x - i) * 9 + (y - j) * 4
                    if t >= 0 and t % 49 == 0:
                        return False
            return True
        if n - i - j >= 0 and check(i, j):
            ans += n - i - j + 1
print(ans)
'\nli = []\nfor i in range(n + 1):\n    for j in range(n - i + 1):\n        for k in range(n - i - j + 1):\n            l = n - i - j - k\n            if not ((i * 50 + j * 10 + k * 5 + l) in li):\n                li.append(i * 50 + j * 10 + k * 5 + l)\nprint(len(li))\n'
