def main():

    def F():
        return map(int, input().split())
    n = int(input())
    groups = [list(F())[::-1] + [i] for i in range(n)]
    k = int(input())
    tables = list(F())
    tables = [[tables[i], i] for i in range(k)]
    tables = sorted(tables)
    groups = sorted(groups)
    count = 0
    SUM = 0
    res = []
    for i in range(n - 1, -1, -1):
        for j in range(len(tables)):
            if tables:
                if groups[i][1] <= tables[j][0]:
                    res.append([groups[i][2], tables[j][1]])
                    count += 1
                    SUM += groups[i][0]
                    tables.pop(j)
                    break
            else:
                return [count, SUM, res]
    return [count, SUM, res]


answer = main()
print(answer[0], answer[1])
for x in answer[2]:
    print(x[0] + 1, x[1] + 1)
