def main():
    N, A, B, C = list(map(int, input().split()))
    d = {'AB': (0, 1), 'AC': (0, 2), 'BC': (1, 2)}
    s = [d[input()] for _ in range(N)]
    abc = [A, B, C]
    ABC = 'ABC'
    ans = []
    for i in range(N):
        x, y = s[i]
        if abc[x] == abc[y] == 0:
            print('No')
            return
        if abc[x] == abc[y] == 1:
            if (i == N - 1) or (x in s[i + 1]):
                ans.append(ABC[x])
                abc[x] += 1
                abc[y] -= 1
            else:
                ans.append(ABC[y])
                abc[x] -= 1
                abc[y] += 1
        else:
            if abc[x] > abc[y]:
                ans.append(ABC[y])
                abc[x] -= 1
                abc[y] += 1
            else:
                ans.append(ABC[x])
                abc[x] += 1
                abc[y] -= 1
    print('Yes')
    for a in ans:
        print(a)


main()
