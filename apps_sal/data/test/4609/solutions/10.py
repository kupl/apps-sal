from sys import stdin, stdout # only need for big input


def solve():
    n = int(input())
    st = set()
    for _ in range(n):
        a = int(input())
        if a in st:
            st.remove(a)
        else:
            st.add(a)
    print(len(st))

def main():
    solve()


def __starting_point():
    main()
__starting_point()
