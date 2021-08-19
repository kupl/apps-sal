def isOk(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if t[i] != '.' and s[i] != t[i]:
            return False
    return True


def main():
    A = ['vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon', 'sylveon']
    n = int(input())
    t = input()
    for s in A:
        if isOk(s, t):
            print(s)
            return


main()
