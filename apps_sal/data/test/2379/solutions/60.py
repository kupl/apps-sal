def main():
    (_n, k, c) = list(map(int, input().split()))
    s = input()
    l = []
    r = []
    for (i, char) in enumerate(s):
        if len(l) >= k:
            break
        if char == 'o' and (not len(l) or i - l[-1] > c):
            l.append(i)
    for (i, char) in reversed(tuple(enumerate(s))):
        if len(r) >= k:
            break
        if char == 'o' and (not len(r) or r[-1] - i > c):
            r.append(i)
    r.reverse()
    for i in range(k):
        if l[i] == r[i]:
            print(l[i] + 1)


main()
