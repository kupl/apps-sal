#!/c/Python34/python
# coding: utf-8


def main():
    N = int(input())
    S = input()
    count = 0
    roomNum = 1
    alpha = [0] * 26
    for (i, s) in enumerate(S):
        if roomNum == N:
            break
        if i % 2 == 0:
            alpha[ord(s)-ord('a')] += 1
        else:
            if alpha[ord(s.lower())-ord('a')] == 0:
                count += 1
            else:
                alpha[ord(s.lower())-ord('a')] -= 1
            roomNum += 1
    print(count)



def __starting_point():
    main()

__starting_point()
