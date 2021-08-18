def count(flight):
    cnt = 0
    for i in range(len(flight)):
        for j in range(14):
            if flight[i][j] == 'S':
                f = [flight[i][j - 1], flight[i][j + 1]]
                cnt += 2 - f.count('-') - f.count('.')
    return cnt


def main():
    n, k = map(int, input().split(' '))
    flight = []
    for i in range(n):
        flight.append(['-'] + list(input()) + ['-'])

    for c in range(3):
        for i in range(n):
            for j in range(14):
                if flight[i][j] == '.' and [flight[i][j - 1], flight[i][j + 1]].count('S') == c:
                    k -= 1
                    flight[i][j] = 'x'
                    if k == 0:
                        return count(flight), '\n'.join([''.join(i[1:-1]) for i in flight])


print(*main(), sep='\n')
