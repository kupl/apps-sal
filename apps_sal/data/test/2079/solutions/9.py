def main():
    n = int(input())
    j = list(map(int, input().split()))
    for i in range(n):
        j[i] = [j[i], i + 1]
    j.sort()
    j = j[::-1]
    e = []
    s = input()
    for i in range(2 * n):
        if s[i] == '0':
            print(j[-1][1], end=' ')
            e.append(j[-1])
            j.pop()
        else:
            print(e[-1][1], end=' ')
            e.pop()
main()
