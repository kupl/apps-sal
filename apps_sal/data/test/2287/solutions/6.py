
def main():
    q = int(input())

    for _ in range(q):
        s = input()
        o = False
        inc = 0
        i = 0
        for x in range(len(s)):
            if s[x] == '1':
                i = x
        for x in range(len(s)):
            if s[x] == '0' and o == True and x < i:
                inc += 1
            if s[x] == '1':
                o = True
        print(inc)


main()
