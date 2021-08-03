from re import split


def main():

    _, k = list(map(int, input().split()))
    s = list(input())
    new_s = []

    for i in range(k):

        if len(s) % 2 == 1:
            s = s * 2

        s = [s[2 * i:2 * i + 2] for i in range(len(s) // 2)]

        for l in s:
            if l[0] == "R":
                if l[1] == "P":
                    new_s.append("P")
                else:
                    new_s.append("R")
            elif l[0] == "S":
                if l[1] == "R":
                    new_s.append("R")
                else:
                    new_s.append("S")
            if l[0] == "P":
                if l[1] == "S":
                    new_s.append("S")
                else:
                    new_s.append("P")

        s = new_s
        new_s = []

    print((s[0]))


main()
