

def main():
    n = int(input())
    st = set()
    st.add(2)
    number = 2
    change = 2

    while number <= n:
        change += 3
        number += change
        st.add(number)
    st = sorted(list(st))
    have = 0
    for i in range(len(st) - 1, -1, -1):
        while n >= st[i]:
            n -= st[i]
            have += 1
    print(have)


def __starting_point():
    t = int(input())
    for i in range(t):
        main()
__starting_point()
