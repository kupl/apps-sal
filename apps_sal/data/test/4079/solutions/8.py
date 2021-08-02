def parse_arr():
    return list(map(int, input().split(' ')))


n = int(input())

for _ in range(n):
    line = input().strip()

    line = sorted(line)

    start = line[0]
    done = False
    for a in line:
        if a == start:
            start = chr(ord(start) + 1)

        else:
            print('No')
            done = True
            break

    if not done:
        print('Yes')
