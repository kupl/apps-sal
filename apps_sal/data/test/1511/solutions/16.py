__author__ = 'Lipen'

def main():
    n, m, k = map(int, input().split())
    data = []
    when = [0]*n
    blockedcells = set()
    blockedcores = set()

    for _ in range(n):
        data.append(list(map(int, input().split())))

    for j in range(m):
        operation = []
        for _ in range(k):
            operation.append([])

        for i in range(n):
            if i not in blockedcores:
                x = data[i][j] - 1
                if x>=0:
                    if x in blockedcells:
                        blockedcores.add(i)
                        when[i] = j+1
                    elif len(operation[x]) > 0:
                        blockedcells.add(x)
                        for core in operation[x]:
                            blockedcores.add(core)
                            when[core] = j+1
                        blockedcores.add(i)
                        when[i] = j+1
                    operation[x].append(i)

    for i in when:
        print(i)

main()
