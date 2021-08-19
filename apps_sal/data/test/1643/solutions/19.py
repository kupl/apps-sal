def main():
    s = input()
    n = len(s)
    st = []
    flags = [False for i in range(n)]
    for i in range(n):
        if s[i] == '1':
            st.append(i)
        elif len(st) != 0:
            st.pop()
    for i in range(len(st)):
        flags[st[i]] = True
    for i in range(n):
        if flags[i] == True:
            print('0', end='')
        else:
            print(s[i], end='')
    print()


main()
