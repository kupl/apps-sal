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

'''
li = []
for i in range(n + 1):
    for j in range(n - i + 1):
        for k in range(n - i - j + 1):
            l = n - i - j - k
            if not ((i * 50 + j * 10 + k * 5 + l) in li):
                li.append(i * 50 + j * 10 + k * 5 + l)
print(len(li))
'''
