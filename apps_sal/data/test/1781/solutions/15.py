def count(flight):
    cnt = 0
    for i in range(len(flight)):
        for j in range(14):
            if flight[i][j] == 'S':
                f = [flight[i][j - 1], flight[i][j + 1]]
                cnt += 2 - f.count('-') - f.count('.')
    return cnt


def main():
    # f = open('B_input.txt', 'rt')
    n, k = map(int, input().split(' '))
    # n, k = map(int, f.readline().split(' '))
    flight = []
    for i in range(n):
        # flight.append(['-'] + list(f.readline().replace('\n', '')) + ['-'])
        flight.append(['-'] + list(input()) + ['-'])
    # f.close()

    for c in range(3):
        for i in range(n):
            for j in range(14):
                if flight[i][j] == '.' and [flight[i][j - 1], flight[i][j + 1]].count('S') == c:
                    k -= 1
                    flight[i][j] = 'x'
                    if k == 0:
                        return count(flight), '\n'.join([''.join(i[1:-1]) for i in flight])


print(*main(), sep='\n')
